import tornado.ioloop
import tornado.web
from pathvalidate import sanitize_filename
from os import listdir
from os.path import isfile

files_path = '/data/'

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    dir_content = listdir(files_path)
    dir_content = map(lambda filename: files_path + filename, dir_content)
    files = filter(isfile, dir_content)
    response = "\n".join(files)
    if response == '':
      response = 'Empty'
    self.write(response)

  def post(self):
    msg = 'Saved:\n'
    for field_name, files in self.request.files.items():
      for info in files:
        filename = sanitize_filename(info["filename"])
        msg += filename
        msg += '\n'
        with open(files_path + filename, 'wb') as out:
          out.write(info["body"])
    self.write(msg)


def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
  ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
