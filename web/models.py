from . import db
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

class Professor(db.Model):
    def __init__(self, email, name):
        self.email = email
        self.name = name

    professor_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    self_introduction = db.Column(db.String(500), nullable=True)
    office_phone = db.Column(db.String(10), nullable=True)
    interest = db.Column(db.String(150), nullable=True)
    

class SchoolExperience(db.Model):
    __tablename__ = "SchoolExperience"
    def __init__(self, school, dept, degree, professor_id):
        
        self.school = school
        self.dept = dept
        self.degree = degree
        self.professor_id = professor_id

    SchoolExperience_id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(50))
    dept = db.Column(db.String(50))
    degree = db.Column(db.String(50))
    professor_id = db.Column(db.ForeignKey("professor.professor_id"))

    professor= db.relationship("Professor", backref="SchoolExperience")

class WorkExperience(db.Model):
    __tablename__ = "WorkExperience"
    def __init__(self,  company_name, position, professor_id):
        self.company_name = company_name
        self.position = position
        self.professor_id = professor_id

    WorkExperience_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50))
    position = db.Column(db.String(50))
    professor_id = db.Column(db.ForeignKey("professor.professor_id"))

    professor= db.relationship("Professor", backref="WorkExperience")

class ClassSchedule(db.Model):
    __tablename__ = "class_schedule"
    def __init__(self, week, time, name, professor_id):
        self.week = week
        self.time = time
        self.name = name
        self.professor_id = professor_id

    schedule_id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer)
    time = db.Column(db.Integer)
    name = db.Column(db.String(20))

    professor_id = db.Column(db.ForeignKey("professor.professor_id"))

    professor = db.relationship("Professor", backref="class_schedules")

class Award(db.Model):
    __tablename__ = "Award"
    def __init__(self, award_name, government, year, awardtime,  professor_id):
        self.award_name = award_name
        self.government = government
        self.year = year
        self.awardtime = awardtime
        self.professor_id = professor_id

    award_id = db.Column(db.Integer, primary_key=True)
    award_name = db.Column(db.String(50))
    government = db.Column(db.String(50))
    year = db.Column(db.Integer)
    awardtime = db.Column(db.String(50))

    professor_id = db.Column(db.ForeignKey("professor.professor_id"))

    professor= db.relationship("Professor", backref="award")

class Paper(db.Model):
    def __init__(self,paper_name,collaborators,page_number_of_the_paper,indexed_website,indexed_time,):
        self.paper_name = paper_name
        self.collaborators = collaborators
        self.page_number_of_the_paper = page_number_of_the_paper
        self.indexed_website = indexed_website
        self.indexed_time = indexed_time

    paper_id = db.Column(db.Integer, primary_key=True)
    paper_name = db.Column(db.String(50))
    collaborators = db.Column(db.String(50))
    page_number_of_the_paper = db.Column(db.String(50))
    indexed_website = db.Column(db.String(150))
    indexed_time = db.Column(db.Date)

    professor_id = db.Column(db.ForeignKey("professor.professor_id"))

    professor = db.relationship("Professor", backref="paper")

    def compare(self, other):
        if self.paper_name != other.paper_name:
            return False
        if self.collaborators != other.collaborators:
            return False
        if self.page_number_of_the_paper != other.page_number_of_the_paper:
            return False
        if self.indexed_website != other.indexed_website:
            return False
        if self.indexed_time != other.indexed_time:
            return False
        
        return True