from flask import Blueprint, request, jsonify
from controllers.assessment_controller import create_assessment
from datetime import datetime

routes = Blueprint('routes', __name__)


@routes.route('/create-assessment', methods=['POST'])
def post_assessment():
    try:
        data = request.get_json()

        # Call the service layer to create the assessment and related data
        assessment = create_assessment(data)

        if not assessment:
            raise Exception("Failed to create assessment.")

        print("Assessment returned from create_assessment:", assessment)
        print("Type of assessment:", type(assessment))

        # getting response data
        response_data = assessment_response(assessment)

        return jsonify(response_data), 200

    except Exception as e:
        print(f"Error in post_assessment: {str(e)}")
        return jsonify({"error": str(e)}), 500




# Helper function to safely handle datetime fields
def format_datetime(dt):
    return dt.isoformat() if isinstance(dt, datetime) else dt

#Function to prepare response of post_assessment
def assessment_response(assessment):
    return {
        "statusCode": 200,
            "body": {
                "Assessment_Id": str(assessment.Assessment_Id),
                "Classroom_Course_Id": assessment.Classroom_Course_Id,
                "Classroom_Course_Work_Id": getattr(assessment, "Classroom_Course_Work_Id", None),
                "Classroom_Coursework_URL": getattr(assessment, "Classroom_Coursework_URL", None),
                "Assessment_Type": assessment.Assessment_Type,
                "Assessment_Que_Image__c": assessment.Assessment_Que_Image__c,
                "Created_As_Premium": getattr(assessment, "Created_As_Premium", "true"),
                "Teacher_Email": getattr(assessment, "Teacher_Email", "appdevelopersdp7@gmail.com"),
                "School__c": assessment.School__c,
                "Name__c": assessment.Name__c,
                "Rubric__c": assessment.Rubric__c,
                "Date__c": format_datetime(assessment.Date__c),
                "Standard__c": assessment.Standard__c,
                "Subject__c": assessment.Subject__c,
                "Teacher__c": assessment.Teacher__c,
                "Google_File_Id": getattr(assessment, "Google_File_Id", None),
                "Session_Id": getattr(assessment, "Session_Id", None),
                "Domain__c": getattr(assessment, "Domain__c", None),
                "Sub_Domain__c": getattr(assessment, "Sub_Domain__c", None),
                "Grade__c": getattr(assessment, "Grade__c", None),
                "Google_Presentation_Id": assessment.Google_Presentation_Id,
                "Status": assessment.Status,
                "AI_Scan": getattr(assessment, "AI_Scan", "true"),
                "Teacher_Contact_Id": getattr(assessment, "Teacher_Contact_Id", None),
                "Enable_Google_Sync": assessment.Enable_Google_Sync,
                "Passage_Id": getattr(assessment, "Passage_Id", None),
                "Class__c": getattr(assessment, "Class__c", None),
                "Active_Status__c": getattr(assessment, "Active_Status__c", "Show"),
                "UpdatedAt": format_datetime(assessment.UpdatedAt),
                "Id": str(assessment.Id) if assessment.Id else None,
                "CreatedDate":format_datetime(assessment.CreatedDate),
                "School_year__c": getattr(assessment, "School_year__c", None),
                "Type__c": getattr(assessment, "Type__c", None),
                "Answer_Key": getattr(assessment, "Answer_Key", None),
                "Teacher_Evaluated_Answer": getattr(assessment, "Teacher_Evaluated_Answer", None),
                "CreatedAt": format_datetime(assessment.CreatedAt),
            }

    }