import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import *
from App.main import create_app
from App.controllers import *




# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')
    print(get_all_employers())
    print(get_all_jobs())
    print(get_all_resumes())
    print(get_all_applications())
    print(get_all_applicants())
    
'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

##EMPLOYER COMMANDS##

employer_cli = AppGroup('employer', help='Employer object commands')

@employer_cli.command('create', help='Create an employer')
@click.option('--company-name', prompt='Please enter company name', )
def create_employer_command(company_name):
    print(create_employer(company_name))

@employer_cli.command('list', help='List all employers')
@click.argument("format", default="string")
def list_employer_command(format):
    if format == 'string':
        print(get_all_employers())


@employer_cli.command('create-job', help='Create a job for applicants')
@click.option("--title",prompt="title", default="Janitor")
@click.option("--description", prompt="description",default="Clean after classes")
@click.option("--requirements", prompt= "requirements", default="Atleast one pass in Csec")
@click.option("--employer-id", prompt="Employer ID", help="The ID of the employer creating the job")
def create_job_command(title, description, requirements, employer_id):
    job = create_job(title, description, requirements, employer_id)
    click.echo(f"Job '{job.title}' created successfully for Employer ID {employer_id}.")

@employer_cli.command('view-applicants', help='lists all applicants')
@click.option('--job-id', prompt='Please enter the Job ID', help='The ID of the job to view applicants', type=int)
def view_applicant_command(job_id):
    applications = get_application_by_job(job_id)
    if not applications:
        print(f'no applicants found!')
    
    for application in applications:
        applicant = get_applicant(application.applicant_id)
        if applicant:
            print(f"Applicant ID: {applicant.id}, Username: {applicant.username}, Email: {applicant.email}, Telephone: {applicant.telephone}, Resume: {applicant.resume_id}")
        else:
            print(f"Could not find applicant with ID {application.applicant_id}")


app.cli.add_command(employer_cli)

##JOB COMMANDS##

job_cli = AppGroup('job', help='Job object commands')

@job_cli.command('list', help='List all available jobs')
def list_job_command():
    print(get_all_jobs())

app.cli.add_command(job_cli)

##RESUME COMMANDS##

resume_cli = AppGroup('resume', help='Resume object commands')

@resume_cli.command('list', help='List all resumes')
@click.argument("format", default="string")
def list_job_command(format):
    if format == 'string':
        print(get_all_resumes())

app.cli.add_command(resume_cli)

##APPLICATION COMMANDS##

application_cli = AppGroup('application', help='Application object commands')

@application_cli.command('list', help='List all Applications')
@click.argument("format", default="string")
def list_job_command(format):
    if format == 'string':
        print(get_all_applications())

app.cli.add_command(application_cli)

##APPLICANT COMMANDS##

applicant_cli = AppGroup('applicant', help='Applicant object commands')

@applicant_cli.command("create", help="Creates an applicant")
@click.option('--username', prompt='Please enter your username', default='', help='ID of the applicant applying for the job')
@click.option('--telephone', prompt='Please enter your phone no.', default='', help='telephone of the applicant applying for the job')
@click.option('--address', prompt='Please enter your address', default='', help='Address of the applicant applying for the job')
@click.option('--email', prompt='Please enter your email', default='', help='email of the applicant applying for the job')
@click.argument("resume_id", default="None")
def create_applicant_command(username, telephone, address, email, resume_id):
    create_applicant(username, telephone, address, email, resume_id)
    print(f'{username} created!')

@applicant_cli.command('list', help='List all applicants')
@click.argument("format", default="string")
def list_job_command(format):
    if format == 'string':
        print(get_all_applicants())

@applicant_cli.command('view-jobs', help='View the jobs available')
def view_jobs_command():
    print(view_jobs())

@applicant_cli.command('apply-for-job', help='Applicant can apply for job')
@click.option('--applicant-id', prompt='Please enter your Applicant ID', type=int, help='ID of the applicant applying for the job')
@click.option('--job-id', prompt='Please enter the Job ID', type=int, help='ID of the job to apply for')
@click.option('--info', prompt='Provide resume info', default='', help='Additional information for the job application')
def apply_for_job_command(applicant_id, job_id, info):
    application = apply_for_job(applicant_id, job_id, info)
    print(f'you have applied, your applicationID is: {application.id}')

app.cli.add_command(applicant_cli)