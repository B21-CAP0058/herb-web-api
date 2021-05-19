from main import db
from sqlalchemy.sql import func

class HerbList(db.Model):
    __tablename__ = 'herb_list'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(120))
    description = db.Column(db.Text)
    efficacy = db.Column(db.Text)
    recipt = db.Column(db.Text)
    image = db.Column(db.Text)
    tags = db.Column(db.Text)
    favorites = db.relationship('favorites', backref='user', lazy='dynamic')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return '<HerbList {}>'.format(self.name)