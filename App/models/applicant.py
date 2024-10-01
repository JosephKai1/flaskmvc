
from App.database import db

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    telephone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'), nullable=True)
    

    def __init__(self, username, telephone, address, email, resume_id=None):
        self.username = username
        self.telephone = telephone
        self.address = address
        self.email = email
        self.resume_id = resume_id
        
    def __repr__(self):
        return f'<ApplicantID: {self.id} - Username: {self.username} - Telephone: {self.telephone} - Address: {self.address} - Email: {self.email} - ResumeID: {self.resume_id}>'


