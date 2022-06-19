import requests

PARAMS = {'id':10}  #указываем константы
URL = 'https://reqres.in/api/users/'


def request_to_api(URL, PARAMS):
    """Функция примает на вход константы, и обращается с заданными параметрами к API"""

    response = requests.get(URL, params=PARAMS).json()

    return (response['data']['first_name'], response['data']['last_name'])

def main():
    print(request_to_api(URL, PARAMS))


if __name__ == '__main__':
    main()
