from App.models import Resume
from App.database import db

def create_resume(info):
    newresume= Resume(info=info)
    db.session.add(newresume)
    db.session.commit()
    return newresume

def get_resume(id):
    return Resume.query.get(id)

def get_all_resumes():
    return Resume.query.all()

def update_resume(id, info):
    resume = get_resume(id)
    if resume:
        resume.info = info
        db.session.add(resume)
        return db.session.commit()
    return None
    