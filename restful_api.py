from flask import Flask,jsonify

app = Flask(__name__)

courses = [
    {
        'name':"AI",
        'course_id':"0",
        'Description':"Introduction to AI"
    },
    {
        'name':"Data Mining",
        'course_id':'1',
        'Description':'Warehouse and mining'
    }
]

@app.route('/')
def index():
    return "Hello Fellow Programmers"

@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses':courses})

@app.route("/courses/<int:course_id>",methods=['GET'])
def get_course(course_id):
    return jsonify({'course': courses[course_id]})

@app.route("/courses", methods=['POST'])
def create():
    course = {
        'name':"Integrative Programming",
        'course_id':'2',
        'Description':'Introduction to REST API'
    }
    courses.append(course)
    return jsonify({'Created':course})

@app.route("/courses/<int:course_id>", methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description'] ="XYZ"
    return jsonify({'course':courses[course_id]})

@app.route("/courses/<int:course_id>", methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'course': "Deleted"})


if __name__ == "__main__":
    app.run(debug=True)