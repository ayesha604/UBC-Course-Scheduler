from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from backend.objects.CoursesLoader import CoursesLoader
from backend.objects.Scheduler import Scheduler

SAVED_COURSES_PATH = './backend/saved_json/saved_courses.json'
NUM_TABLES = 20


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
        course_names1 = loader.get_course_names_term(1)
        course_names2 = loader.get_course_names_term(1)
        response = {"Term 1": course_names1,
                    "Term 2": course_names2}
        return jsonify(response)

    @app.route('/schedule', methods=['POST', 'OPTIONS'])
    @cross_origin(allow_headers=['Content-Type'])
    def schedule():
        data = request.get_json()
        course_names = data['courses']
        term = data['term']
        courses = loader.get_courses_from_names(course_names)
        scheduler = Scheduler()
        scheduler.schedule(courses, term)
        # for timetable in scheduler.getTopTimetables(1):
        #     sections = timetable.getSections()
        #     print(f"Timetable with score {timetable.getScore()}")
        #     for section in sections:
        #         print(f"{section.name} : {section.times}")
        #     print()

        return jsonify(scheduler.to_dict(NUM_TABLES))

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
