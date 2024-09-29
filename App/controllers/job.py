from App.models import Job
from App.database import db

def create_job(title, description, requirements):
    newJob = Job(title=title, description=description, requirements=requirements)
    db.session.add(newJob)
    db.session.commit()
    return newJob

def get_job_by_title(title):
    return Job.query.filter_by(title=title).first()

def get_job(id):
    return Job.query.get(id)

def get_all_jobs():
    return Job.query.all()

def update_job(id, title, description, requirements, employerName):
    job = get_job(id)
    if job:
        job.id = id
        job.title = title
        job.description = description
        job.requirements = requirements
        job.employerName = employerName
        db.session.add(job)
        return db.session.commit()
    return None