from App.models import Application
from App.database import db
from App.models import *

def create_application(applicant_id, job_id):
    newapplication = Application(applicant_id=applicant_id, job_id=job_id)
    db.session.add(newapplication)
    db.session.commit()
    return newapplication

def get_application(id):
    return Application.query.get(id)

def get_all_Applications():
    return Application.query.all()

def update_Application(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
