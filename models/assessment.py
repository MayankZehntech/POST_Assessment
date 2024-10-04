from services.database import db
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Assessment(db.Model):
    __tablename__ = 'Assessment__c'

    # Primary Key
    Assessment_Id = db.Column(db.Text, primary_key=True)

    # Other columns
    Name__c = db.Column(db.Text, nullable=True)
    CreatedAt = db.Column(db.DateTime, nullable=True)
    Date__c = db.Column(db.Text, nullable=True)
    Rubric__c = db.Column(db.Text, nullable=True)
    School__c = db.Column(db.Text, nullable=True)
    School_year__c = db.Column(db.Text, nullable=True)
    Standard__c = db.Column(db.Text, nullable=True)
    Subject__c = db.Column(db.Text, nullable=True)
    Teacher__c = db.Column(db.Text, nullable=True)
    Type__c = db.Column(db.Text, nullable=True)
    Session_Id = db.Column(db.Text, nullable=True)
    Teacher_Contact_Id = db.Column(db.Text, nullable=True)
    Teacher_Email = db.Column(db.Text, nullable=True)
    Created_As_Premium = db.Column(db.Text, nullable=True)
    Domain__c = db.Column(db.Text, nullable=True)
    Sub_Domain__c = db.Column(db.Text, nullable=True)
    Grade__c = db.Column(db.Text, nullable=True)
    Assessment_Que_Image__c = db.Column(db.Text, nullable=True)
    Answer_Key = db.Column(db.Text, nullable=True)
    Assessment_Type = db.Column(db.Text, nullable=True)
    Classroom_Course_Id = db.Column(db.Text, nullable=True)
    Classroom_Coursework_URL = db.Column(db.Text, nullable=True)
    Google_Presentation_Id = db.Column(db.Text, nullable=True)
    Status = db.Column(db.Text, nullable=True)
    AI_Scan = db.Column(db.Text, nullable=True)
    UpdatedAt = db.Column(db.DateTime, nullable=True, onupdate=datetime.now())
    Enable_Google_Sync = db.Column(String(50), nullable=True)
    Passage_Id = db.Column(db.Text, ForeignKey('Assessment_Reading_Passage.Id'), nullable=True)
    Tokens_Consumed = db.Column(db.Text, nullable=True)

    OwnerId = db.Column(db.Text, nullable=True)
    IsDeleted = db.Column(db.String(50), nullable=True)
    Name = db.Column(db.String(255), nullable=True)
    CreatedDate = db.Column(db.DateTime, nullable=True)

    LastModifiedDate = db.Column(db.Text, nullable=True)
    SystemModstamp = db.Column(db.Text, nullable=True)
    CreatedById = db.Column(db.Text, nullable=True)
    LastModifiedById = db.Column(db.Text, nullable=True)
    LastViewedDate = db.Column(db.Text, nullable=True)
    LastReferencedDate = db.Column(db.Text, nullable=True)
    ConnectionReceivedId = db.Column(db.Text, nullable=True)
    ConnectionSentId = db.Column(db.Text, nullable=True)
    Google_File_Id = db.Column(db.Text, nullable=True)
    Classroom_Course_Work_Id = db.Column(db.Text, nullable=True)
    Id = db.Column(db.BigInteger, nullable=False, server_default=db.text("nextval('id_sequence')"))
    Class__c = db.Column(db.Text, nullable=True)
    Active_Status__c = db.Column(db.Text, nullable=True)
    Teacher_Evaluated_Answer = db.Column(db.Text, nullable=True)




    

    # Relationship to `Assessment_Reading_Passage`
    reading_passage = relationship("AssessmentReadingPassage", back_populates="assessment")
    





class AssessmentReadingPassage(db.Model):
    __tablename__ = 'Assessment_Reading_Passage'

    # Primary Key
    Id = db.Column(db.BigInteger, primary_key=True)

    # Other columns
    CreatedAt = db.Column(db.DateTime, nullable=True)
    UpdatedAt = db.Column(db.DateTime, nullable=True)
    Attachment_URL = db.Column(db.String(255), nullable=True)

    # Relationship to `Assessment__c`
    assessment = relationship("Assessment", back_populates="reading_passage")

    # Relationship to `Assessment_Reading_Passage_Attachment`
    attachments = relationship("AssessmentReadingPassageAttachment", back_populates="reading_passage")




class AssessmentReadingPassageAttachment(db.Model):
    __tablename__ = 'Assessment_Reading_Passage_Attachment'

    # Primary Key
    Id = db.Column(db.BigInteger, primary_key=True)

    # Foreign Key to `Assessment_Reading_Passage`
    Passage_Id = db.Column(db.BigInteger, ForeignKey('Assessment_Reading_Passage.Id'), nullable=False)

    # Other columns
    Attachment_URL = db.Column(db.Text, nullable=True)
    Sorting_Order = db.Column(db.Integer, nullable=True)
    Status = db.Column(db.String(50), nullable=True)
    CreatedAt = db.Column(db.DateTime, nullable=True)
    UpdatedAt = db.Column(db.DateTime, nullable=True)

    # Relationship to `Assessment_Reading_Passage`
    reading_passage = relationship("AssessmentReadingPassage", back_populates="attachments")
