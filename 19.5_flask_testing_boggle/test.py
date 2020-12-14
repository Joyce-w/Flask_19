from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self) :
        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_homepage(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<title>Boggle</title>', html)

    #failes if test_is_word is present?
    def test_sessions(self):
        with app.test_client() as client:
            res = client.get('/')
            self.assertTrue(session['game_board'])

    def test_is_word(self):
        with app.test_client() as client:
            res = self.client.get('/answers?submitted=mo')
            self.assertEqual(res.json[result], "ok")
 
# test for high score
# test for result content
# test session results