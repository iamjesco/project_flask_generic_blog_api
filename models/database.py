from app import db
from datetime import datetime
import re


class Post(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    slug = db.Column(db.String(250), nullable=False, unique=True)
    body = db.Column(db.Text(), nullable=False)
    author = db.Column(db.String(100), default='Jesco')
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    status = db.Column(db.String(250), nullable=False)
    featured = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'{self.title}'

    def __init__(self, title, body, status, featured):
        self.title = title
        self.slug = re.sub('[ ]', '-', self.title.lower())
        self.body = body
        self.status = status
        self.featured = featured

