from backend.objects.CoursesLoader import CoursesLoader

SAVED_COURSES_PATH = './backend/saved_json/saved_courses.json'

def main():
    loader = CoursesLoader()
    loader.load(SAVED_COURSES_PATH)
    print(loader.get_course_names_term(1))
    print(loader.get_course_names_term(2))


if __name__ == '__main__':
    main()
