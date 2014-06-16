from google.appengine.ext import ndb

default_depot_key = "tc-depots"

def depot_key(key_name=default_depot_key):
    return ndb.Key('Depot', key_name)

class Depot(ndb.Model):
    name = ndb.StringProperty()