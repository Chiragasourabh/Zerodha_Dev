import random
import string

import cherrypy


class StringGenerator(object):

    @cherrypy.expose
    def search(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

    @cherrypy.expose
    def table(self):
        return "This is how it works"

    @cherrypy.expose
    def retHello():
        return "Hello"


    @cherrypy.expose
    def testFun(self):
        return retHello()


    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="post" action="search">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())