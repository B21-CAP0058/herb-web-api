from main import db
from sqlalchemy.sql import func

class History(db.Model):
    __tablename__ = 'histories'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(64), index=True, unique=True)
    image = db.Column(db.Text)
    result = db.Column(db.Text)
    herb_likely_id = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return '<History {}>'.format(self.result)