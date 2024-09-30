from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'),nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

    def __repr__(self):
        return f'<Application {self.id} - {self.applicant_id} - {self.job_id}>'
    