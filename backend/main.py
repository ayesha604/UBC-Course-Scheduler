from flask import Flask, request, jsonify

from backend.objects.CoursesLoader import CoursesLoader


SAVED_COURSES_PATH = './backend/saved_json/saved_courses.json'


def main():
    app = Flask(__name__)

    loader = CoursesLoader()
    loader.load(SAVED_COURSES_PATH)

    @app.route('/valid_courses', methods=['GET'])
    def valid_courses():
        # TODO: separate by term
        course_names = loader.get_course_names()
        response = {"Term 1": course_names,
                    "Term 2": course_names}
        return jsonify(response)

    @app.route('/schedule', methods=['POST'])
    def schedule():
        course_names = request.get_json()['courses']
        print(course_names)
        # return data

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
