import os

from depot import Depot
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class DepotMainPage(webapp2.RequestHandler):

    def get(self):
        depots_query = Depot.query(
            ancestor=ndb.Key('Depot', 'tc-depots')
        ).order(+Depot.name)

        depots = depots_query.fetch()

        template_values = {
            'depots' : depots,
        }

        template = JINJA_ENVIRONMENT.get_template('templates/depots.html')
        self.response.write(template.render(template_values))


class DepotAdd(webapp2.RequestHandler):

    def post(self):
        depot = Depot(parent=ndb.Key('Depot', 'tc-depots'))
        depot.name = self.request.get('depotname')
        depot.put()
        self.redirect('/depots')


app = webapp2.WSGIApplication([
    ('/depots', DepotMainPage),
    ('/depots/add', DepotAdd)
], debug=True)