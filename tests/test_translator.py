import unittest
import app
import requests


class AppTest(unittest.TestCase):
    def setUp(self) -> None:
        self.response = requests.get(app.URL, params={'key': app.API_KEY, 'text': 'Hello',
                                                      'lang': 'ru', })

    def test_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_translate(self):
        app_return = app.translate_it('Hello')
        self.assertEqual(app_return, 'Привет')

    def test_lang(self):
        self.assertRaises(KeyError, app.translate_it, 'Hello', 'ge') # Отрицательный тест, когда язык введен неверно
