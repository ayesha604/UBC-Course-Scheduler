from backend.objects.CoursesLoader import CoursesLoader

SAVED_COURSES_PATH = './backend/saved_json/saved_courses.json'


def main():
    loader = CoursesLoader()
    loader.load(SAVED_COURSES_PATH)
    courses = loader.get_courses_from_names(['CPSC 110', 'MATH 100'])
    for course in courses:
        print(course)


if __name__ == '__main__':
    main()
