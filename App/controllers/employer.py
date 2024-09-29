from App.models import Employer
from App.database import db
from App.controllers.job import ( create_job )


def create_employer(companyName):
    newEmployer = Employer(companyName=companyName)
    db.session.add(newEmployer)
    db.session.commit()
    return newEmployer

def get_all_employers():
    return Employer.query.all()

def get_employer(id):
    return Employer.query.get(id)

def update_employer(id, comapanyName):
    employer = get_employer(id)
    if employer:
        employer.companyNameame = comapanyName
        db.session.add(employer)
        return db.session.commit()
    return None
