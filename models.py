from google.appengine.ext import db


class UserAccount(db.Model):
    """Models an application user."""
    user_id = db.StringProperty()
    user = db.UserProperty()
    is_axis_admin = db.BooleanProperty()


class Depot(db.Model):
    name = db.StringProperty()
    editor = db.ReferenceProperty(reference_class=UserAccount)

class AccidentReport(db.Model):
    user_account = db.ReferenceProperty(reference_class=UserAccount)
    depot = db.ReferenceProperty(reference_class=Depot)
    near_miss = db.IntegerProperty()
    dangerous_occurrence = db.IntegerProperty()
    minor = db.IntegerProperty()
    lost_time_injury = db.IntegerProperty()
    major = db.IntegerProperty()
    death = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)