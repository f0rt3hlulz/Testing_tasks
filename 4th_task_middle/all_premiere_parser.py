import json

import requests
from bs4 import BeautifulSoup

URL = 'https://www.kinopoisk.ru/premiere/ru/'
HEADERS = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'
}


def make_request(URL):
    '''Функция выполняет запрос по заданному URL страницы с премьерами
    кинопоиска, парсит информацию и возвращает JSON ответ.'''

    json_data = []

    for page_number in range(1, 9):
        response = requests.get(url=f'{URL}page/{page_number}/', headers=HEADERS)
        soup = BeautifulSoup(response.text, 'lxml')
        soup_find = soup.find_all('div', class_='premier_item')
        
        for film in soup_find:
            parsed_data = {}
            parsed_data['name'] = film.find('div', class_='textBlock').find('a').text
            parsed_data['name_eng'] = film.find('div', class_='textBlock').find('a').next_element.next_element.next_element.text
            parsed_data['film_link'] = 'https://www.kinopoisk.ru/' + film.find('a').get('href')
            if film.find('span', class_='ajax_rating').find('u'):
                film_rating = film.find('span', class_='ajax_rating').find('u').text.strip()
                parsed_data['film_rating'] = film_rating.partition('\xa0')[0]
            #if film.find('span', class_='ajax_rating await_rating').find('b'):
            #    parsed_data['wait_rating'] = film.find('span', class_='ajax_rating await_rating').find('b').text.strip()
            #else:
            #    parsed_data['wait_rating'] = 'None'
            # При обращении и поиска по классу рейтинга ожидания - выдаёт пустой список
            parsed_data['wait_rating'] = 'None'
            if film.find('span', class_='ajax_rating').find('b'):
                parsed_data['votes'] = film.find('span', class_='ajax_rating').find('b').text.strip()
            parsed_data['date'] = film.find('meta').get('content')
            parsed_data['company'] = film.find('s', class_='company').find('a').text
            genres = film.find('div', class_='textBlock').find_all('span')[3].text
            if genres:
                parsed_data['genres'] = film.find('div', class_='textBlock').find_all('span')[3].text
            else:
                parsed_data['genres'] = 'None'
            json_data.append(parsed_data)

    return json.dumps(json_data, indent=4, ensure_ascii=False)

# def write_in_file(data):
#     '''Функция записи ответа в JSON файл'''
#     with open('json_data.json', 'w') as file:
#         file.write(data)
#     file.close


def main():
    if requests.get(url=URL).status_code != 200:
        raise ConnectionError('Сервис недоступен.')
    try:
        print(make_request(URL))
        # data = make_request(URL)
        # write_in_file(data)
    except Exception as error:
        print(f'Сбой в работе программы {error}')


if __name__ == '__main__':
    main()
