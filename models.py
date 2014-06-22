from google.appengine.ext import db

def is_valid_depot_name(val):
    if len(str(val).strip()) < 1:
        raise db.BadValueError

class UserAccount(db.Model):
    user_id = db.StringProperty()
    user = db.UserProperty()
    is_axis_admin = db.BooleanProperty()


class Depot(db.Model):
    name = db.StringProperty(validator=is_valid_depot_name)
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