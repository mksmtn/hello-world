from tornado.testing import AsyncHTTPTestCase, main
from os import environ

import app

expected_response = 'Test: Hello, world' if environ['environment'] == 'test' else 'Hello, world'

class TestHelloApp(AsyncHTTPTestCase):
  def get_app(self):
    return app.make_app()

  def test_homepage(self):
    response = self.fetch('/')
    self.assertEqual(response.code, 200)
    self.assertEqual(response.body.decode('utf-8'), expected_response)

if __name__ == '__main__':
  main()
