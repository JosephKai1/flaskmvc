from App.models import Applicant
from App.database import db

def create_applicant(username, telephone, address, email, resume_id):
    newapplicant = Applicant(username=username, telephone=telephone, address=address, email=email, resume_id=resume_id)
    db.session.add(newapplicant)
    db.session.commit()
    return newapplicant

def get_applicant_by_username(username):
    return Applicant.query.filter_by(username=username).first()

def get_applicant(id):
    return Applicant.query.get(id)

def get_all_applicants():
    return Applicant.query.all()

def update_applicant(id, username, telephone, address, email, resume_id):
    applicant = get_applicant(id)
    if applicant:
        applicant.username = username
        db.session.add(applicant)
        return db.session.commit()
    return None
    