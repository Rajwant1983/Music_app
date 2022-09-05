from flask import render_template
from application.app import application
from application.schema import *

@application.route('/')
def root():
    return render_template('root.html')

@application.route('/colleges')
def college_list():
    all_students = Colleges.query.all()
    return render_template('all_colleges.html',list_of_names=all_colleges)

@application.route('/colleges/<int:id>')
def foreign_language(id):
    program_of_specific_college = Programs.query.filter_by(college_id=id)
