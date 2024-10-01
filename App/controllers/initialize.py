from .user import create_user
from .applicant import create_applicant
from .application import create_application
from .employer import create_employer
from .job import create_job
from .resume import create_resume
from App.database import db

def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_resume('8 1s in Csec')
    create_applicant('bob', '777-2223', '#23 Tacarigua', 'bob@mail.com', 'None')    
    create_job('Software Engineer', 'create software given user requirements', '1 in Csec IT', '1')
    create_employer('Microsoft')
