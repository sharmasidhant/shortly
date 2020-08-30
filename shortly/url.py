from .db import db

class Url(db.Document):
    original_url = db.StringField(required=True, unique=True)
    short_url = db.StringField()
    created_at = db.DateTimeField(required=True)
