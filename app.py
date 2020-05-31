import requests
import config

API_KEY = config.app_key
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text_to_translate, to_lang='ru'):
    params = {
        'key': API_KEY,
        'text': text_to_translate,
        'lang': '{}'.format(to_lang),
    }
    response = requests.get(URL, params=params)
    print('Запрос к URL для перевода')
    json_ = response.json()
    return ''.join(json_['text'])


if __name__ == '__main__':
    text_to_translate = input('Введите текст, который хотите перевести - ')
    lang = input('Введите язык, на который хотите перевести текст - ')

    print(translate_it(text_to_translate, lang))
