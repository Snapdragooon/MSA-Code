import flask
from flask import request, jsonify
import student_generator_v2 as sg

# create a flask app object
app = flask.Flask(__name__)

# tell the server to reload each time the code changes
app.config["DEBUG"] = True

# load student dictionaries

# create a route to display our name
@app.route('/', methods=['GET'])
def index():
    return "<h1> My name is Sophie Sheahan</h1>"

# create a route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    # load student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

# create a route to return students by major
@app.route('/api/majors/<string:major>', methods=['GET'])
def api_students_by_major(major:str):
    print(major)
    # get students with major major
    # get all students
    student_dictionaries = sg.get_student_dictionaries()
    major_students = []

    # use for loop to search
    for student in student_dictionaries:
        if major == student['major']:
            major_students.append(student)

    return major_students

# create 2 routes
# - return all student data
# - return students by major

# run the application
app.run()
