from google.appengine.ext import ndb


class Depot(ndb.Model):
    name = ndb.StringProperty()