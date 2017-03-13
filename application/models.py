from mongokit import Document, Connection
from application import db
import datetime


@db.register
class Video(Document):
    __collection__ = 'latenightstats'
    __database__ = 'video'
    structure = {
        'id': basestring,
        'title': basestring,
        'channel': basestring,
    }
    required_fields = ['vid', 'title', 'channel']
