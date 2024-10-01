from App.models import Applicant
from App.database import db
from App.controllers.job import *
from App.controllers.application import *
from App.controllers.resume import *


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
        applicant.id = id
        applicant.username = username
        applicant.telephone = telephone
        applicant.address = address
        applicant.email = email
        applicant.resume_id = resume_id
        db.session.add(applicant)
        return db.session.commit()
    return None

def view_jobs():
    jobs = get_all_jobs()
    if jobs:
        return jobs
    return "No jobs available"

def apply_for_job(applicant_id, job_id, info):
    newresume = create_resume(info)
    application = create_application(applicant_id=applicant_id, job_id=job_id)
    return application