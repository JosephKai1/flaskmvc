
from App.database import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    requirements = db.Column(db.String(100), nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
    employer = db.relationship('Employer', backref=db.backref('jobs', lazy='joined'))
    applicants = db.relationship('Applicant', secondary='application', backref=db.backref('jobs', lazy=True))

def __init__(self, title, description, requirements, employerName):
    self.title = title
    self.description = description
    self.requirements = requirements
    self.employerName = employerName

def __repr__(self):
        return f'<JobTitle {self.title} - Description{self.description} - Requirements{self.requirements} - EmployerID{self.employer_id}>'