from tornado.testing import AsyncHTTPTestCase, main
from os import makedirs

import app


class TestHelloApp(AsyncHTTPTestCase):
  def get_app(self):
    return app.make_app()

  def test_homepage(self):
    makedirs('/data', exist_ok=True)
    response = self.fetch('/')
    self.assertEqual(response.code, 200)
    self.assertEqual(response.body.decode('utf-8'), 'Empty')

if __name__ == '__main__':
  main()
