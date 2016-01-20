import os
import webapp2

from google.appengine.api import modules


class MainPage(webapp2.RequestHandler):
  def get(self):
    # self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World!')
    self.response.write("<p>Version (os.environ['CURRENT_VERSION_ID']): " + 
      os.environ['CURRENT_VERSION_ID'] + '</p>')
    self.response.write("<p>modules.get_current_version_name(): " + 
      modules.get_current_version_name() + "</p>")
    self.response.write("<p>Request Host: " + 
      self.request.headers['Host'] + "</p>")
    self.response.write("<p>Custom environment variable: DEVELOPERTIPS_CUSTOM_ENV='" +
      os.environ['DEVELOPERTIPS_CUSTOM_ENV'] + "'</p>" )
app = webapp2.WSGIApplication([
  ('/helloworld', MainPage),
], debug = True)