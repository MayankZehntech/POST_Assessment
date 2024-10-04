from services.database import db
from flask import jsonify
from models.assessment import Assessment, AssessmentReadingPassage, AssessmentReadingPassageAttachment
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
import uuid


def create_assessment(data):
    try:
        # Check if Assessment_Id is provided
        assessment_id = data.get("Assessment_Id")

        if assessment_id:
            # If Assessment_Id is provided, try to find the existing record
            assessment = Assessment.query.filter_by(Assessment_Id=assessment_id).first()

            if not assessment:
                return jsonify({"error": f"Assessment with ID {assessment_id} not found."}), 404
        else:
            # If Assessment_Id is not provided, generate a unique ID
            assessment_id = str(uuid.uuid4().int)[:23]
            assessment = Assessment(Assessment_Id=assessment_id)

        # Update or set fields
        assessment.Name__c = data.get("Name__c")
        assessment.CreatedDate = assessment.CreatedDate or datetime.now()  # Set creation date only if not previously set
        assessment.Date__c = data.get("Date__c")
        assessment.Rubric__c = data.get("Rubric__c")
        assessment.School__c = data.get("School__c")
        assessment.Standard__c = data.get("Standard__c")
        assessment.Subject__c = data.get("Subject__c")
        assessment.Teacher__c = data.get("Teacher__c")
        assessment.Assessment_Que_Image__c = data.get("Assessment_Que_Image__c")
        assessment.Assessment_Type = data.get("Assessment_Type")
        assessment.Session_Id = data.get("Session_Id")
        assessment.Teacher_Contact_Id = data.get("Teacher_Contact_Id")
        assessment.Teacher_Email = data.get("Teacher_Email")
        assessment.Created_As_Premium = data.get("Created_As_Premium")
        assessment.Domain__c = data.get("Domain__c")
        assessment.Sub_Domain__c = data.get("Sub_Domain__c")
        assessment.Grade__c = data.get("Grade__c")
        assessment.Status = data.get("Status")
        assessment.AI_Scan = data.get("AI_Scan")
        assessment.Enable_Google_Sync = data.get("Enable_Google_Sync")
        assessment.Google_Presentation_Id = data.get("Google_Presentation_Id")
        assessment.Tokens_Consumed = data.get("Tokens_Consumed")
        assessment.UpdatedAt = datetime.now()

        db.session.add(assessment)
        db.session.flush()  # This generates the Assessment entry without committing

        # Create or update Reading Passage entry (if provided)
        if "Passage_Attachments" in data and data["Passage_Attachments"]:
            if not assessment.Passage_Id:
                # Create a new passage if it doesn't exist
                passage = AssessmentReadingPassage(
                    CreatedAt=datetime.now(),
                    UpdatedAt=datetime.now()
                )
                db.session.add(passage)
                db.session.flush()
                assessment.Passage_Id = passage.Id
            else:
                # Update the existing passage
                passage = AssessmentReadingPassage.query.filter_by(Id=assessment.Passage_Id).first()

            # Handle Reading Passage Attachments
            for attachment_data in data.get("Passage_Attachments", []):
                attachment = AssessmentReadingPassageAttachment(
                    Passage_Id=passage.Id,
                    Attachment_URL=attachment_data.get("Attachment_URL"),
                    Sorting_Order=attachment_data.get("Sorting_Order"),
                    Status="Active",  # Set a default status if required
                    CreatedAt=datetime.now(),
                    UpdatedAt=datetime.now()
                )
                db.session.add(attachment)

        db.session.commit()

        return assessment
       

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback on error
        print(f"Error in create_assessment: {str(e)}")
        raise