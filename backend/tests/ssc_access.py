import requests


def check_access() -> bool:
    url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-all-departments'

    headers = {
        'User-Agent': 'very real human',
        'From': 'human@realperson.com'
    }

    response = requests.get(url, headers=headers)
    # response = requests.get(url)
    if response.content.find(b'CPSC') != -1:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_access())
