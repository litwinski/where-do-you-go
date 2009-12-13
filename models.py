from google.appengine.ext import db
from geo.geomodel import GeoModel

class AuthToken(db.Model):
  service = db.StringProperty(required=True)
  token = db.StringProperty(required=True)
  secret = db.StringProperty(required=True)
  created = db.DateTimeProperty(auto_now_add=True)

class UserInfo(db.Model):
  user = db.UserProperty()
  last_checkin = db.IntegerProperty()
  created = db.DateTimeProperty(auto_now_add=True)
  token = db.StringProperty()
  secret = db.StringProperty()

class UserVenue(GeoModel):
  user = db.UserProperty()
  checkin_list = db.ListProperty(int, default=[])
  last_updated = db.DateTimeProperty(auto_now_add=True)
  venue_id = db.IntegerProperty()
  name = db.StringProperty()
  address = db.StringProperty()
  cross_street = db.StringProperty()
  city = db.StringProperty()
  state = db.StringProperty()
  zipcode = db.StringProperty()
  phone = db.PhoneNumberProperty()

class MapImage(db.Model):
  user = db.UserProperty() # user_id and not a user so that it can be in the URL later on????
  user_id = db.StringProperty() # TODO figure out how to query for UserPropertys by user_id
  centerlat = db.FloatProperty()
  centerlong = db.FloatProperty()
  northlat = db.FloatProperty()
  westlong = db.FloatProperty()
  zoom = db.IntegerProperty()
  width = db.IntegerProperty()
  height = db.IntegerProperty()
  img = db.BlobProperty()

