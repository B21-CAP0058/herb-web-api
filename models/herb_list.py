from main import db
from sqlalchemy.sql import func
import csv

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
    #favorites = db.relationship('favorites', backref='user', lazy='dynamic')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return '<HerbList {}>'.format(self.name)
    
    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'uuid': self.uuid,
            'name': self.name,
            'description': self.description,
            'efficacy': self.efficacy,
            'recipt': self.recipt,
            'image': self.image,
            'tags': self.tags,
            'is_favorited': 0,
            'created_at': self.created_at
        }
    
    @staticmethod
    def import_data():
        """ Import to table herb_list from csvfile """
        with open('data/dataset-0.1.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Id']:
                    data = HerbList(uuid=row['Id'],
                                    name=row['Name'],
                                    description=row['Deskripsi'],
                                    efficacy=row['Khasiat'],
                                    recipt=row['Resep'],
                                    tags=row['Tag'],
                                    image=row['Image'])
                    db.session.add(data)
                    try:
                        db.session.commit()
                    except:
                        db.session.rollback()
