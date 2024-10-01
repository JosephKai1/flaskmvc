from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(5000), nullable=True)
    applicants = db.relationship('Applicant', backref='resume')

    def __init__(self, info):
        self.info = info

    def __repr__(self):
        return f'<Resume {self.id} - {self.info}>'
