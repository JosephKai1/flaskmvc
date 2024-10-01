from App.models import Employer
from App.database import db
from App.controllers.job import *
from App.controllers.applicant import *


def create_employer(companyName):
    newEmployer = Employer(companyName=companyName)
    db.session.add(newEmployer)
    db.session.commit()
    return newEmployer

def get_all_employers():
    return Employer.query.all()

def get_employer(id):
    return Employer.query.get(id)

def get_employer_by_name(companyName):
    return Employer.query.filter_by(companyName=companyName).first()

def update_employer(id, comapanyName):
    employer = get_employer(id)
    if employer:
        employer.companyNameame = comapanyName
        db.session.add(employer)
        return db.session.commit()
    return None

def create_job(title, description, requirements, employer_id):
    employer = Employer.query.get(employer_id)
    job = create_job(title, description, requirements,employer_id)
    return job

def view_applicants():
    all_applicants = get_all_applicants()
    return all_applicants