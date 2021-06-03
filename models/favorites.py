from main import db
from sqlalchemy.sql import func

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    herb_id = db.Column(db.Integer, db.ForeignKey('herb_list.id'))
   
    def __repr__(self):
        return '<Favorites: User Id {} Herb Id {}>'.format(self.user_id, self.herb_id)