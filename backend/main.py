from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from backend.objects.CoursesLoader import CoursesLoader
from backend.objects.Scheduler import Scheduler

SAVED_COURSES_PATH = './backend/saved_json/saved_courses.json'


def main():
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['CORS_ORIGIN'] = '*'

    loader = CoursesLoader()
    loader.load(SAVED_COURSES_PATH)

    @app.route('/valid_courses', methods=['GET'])
    @cross_origin()
    def valid_courses():
        # TODO: separate by term
        course_names = loader.get_course_names()
        response = {"Term 1": course_names,
                    "Term 2": course_names}
        return jsonify(response)

    @app.route('/schedule', methods=['POST'])
    @cross_origin()
    def schedule():
        data = request.get_json()['courses']
        course_names = data
        courses = loader.get_courses_from_names(course_names)
        scheduler = Scheduler()
        # TODO: pass in term
        scheduler.schedule(courses, 1)
        ...

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
