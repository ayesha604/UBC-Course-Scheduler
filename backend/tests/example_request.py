import requests


def send_example():
    data = {"body": {
        "1": [],
        "2": []
    }}
    res = requests.post('http://127.0.0.1:5000/schedule', json=data)
    if res.ok:
        print(res.json())


if __name__ == '__main__':
    send_example()
