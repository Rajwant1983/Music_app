#routes and connectivity
from flask import render_template
from tests.application.app import application
from tests.application.schema import *

@application.route('/')
def root():
    return render_template('root.html')

@application.route('/colleges')
def college_list():
    all_colleges = Colleges.query.all()
    return render_template('all_colleges.html',list_of_names=all_colleges)

@application.route('/college/<int:id>')
def programs(id):
    program_of_specific_college = Programs.query.filter_by(college_id=id)
    college = Colleges.query.get(id)
    return render_template('all_programs.html',list_of_names=program_of_specific_college,college=college)