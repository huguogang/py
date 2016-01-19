import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World! Version 1')
   
app = webapp2.WSGIApplication([
  ('/helloworld', MainPage),
], debug = True)