from google.appengine.ext import ndb


class UserAccount(ndb.Model):
    """Models an application user."""
    user_id = ndb.StringProperty()
    user = ndb.UserProperty()
    is_axis_admin = ndb.BooleanProperty()


class Depot(ndb.Model):
    name = ndb.StringProperty()