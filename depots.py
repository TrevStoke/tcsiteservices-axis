from google.appengine.api import users

import webapp2
import jinja2
import os

from models import Depot
from models import UserAccount

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class DepotHandler(webapp2.RequestHandler):
    def get(self):
        depots = Depot.all()

        template_values = {
            'depots': depots,
        }

        template = JINJA_ENVIRONMENT.get_template('templates/depots.html')

        self.response.write(template.render(template_values))

    def post(self):
        depot = Depot()
        depot.name = self.request.get('depotname')
        depot.put()
        self.redirect('/depots')

app = webapp2.WSGIApplication([
    ('/depots', DepotHandler),
    ('depots/', DepotHandler),
    ('/depots/add', DepotHandler),
], debug=True)