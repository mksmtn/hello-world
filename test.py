from tornado.testing import AsyncHTTPTestCase, main

import app


class TestHelloApp(AsyncHTTPTestCase):
  def get_app(self):
    return app.make_app()

  def test_homepage(self):
    response = self.fetch('/')
    self.assertEqual(response.code, 200)
    self.assertEqual(response.body.decode('utf-8'), 'Test: Hello, world')

if __name__ == '__main__':
  main()
