from main import db
from sqlalchemy.sql import func

class PremiumStatus(db.Model):
    __tablename__ = 'premium_status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    code = db.Column(db.String(64))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<PremiumStatus {}>'.format(self.name)