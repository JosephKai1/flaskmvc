from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'),nullable=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=True)

    def __init__(self, applicant_id, job_id):
        self.applicant_id = applicant_id
        self.job_id = job_id
        

    def __repr__(self):
        return f'<ApplicationID: {self.id} - ApplicantID: {self.applicant_id} - JobID: {self.job_id}>'
    