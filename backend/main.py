import json
from flask import Flask, request, jsonify


def main():
    app = Flask(__name__)

    @app.route('/valid_courses', methods=['GET'])
    def valid_courses():
        return "Valid Courses Placeholder"

    @app.route('/schedule', methods=['POST'])
    def schedule():
        data = request.get_json()['body']
        return data

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
