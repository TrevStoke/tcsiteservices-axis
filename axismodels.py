
from google.appengine.ext import ndb


class AxisUser(ndb.Model):
    """Models an application user."""
    uniqueKey = ndb.StringProperty()
    name = ndb.StringProperty()