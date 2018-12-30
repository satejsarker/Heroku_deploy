
from db import  db

class StoreModel(db.Model):
    __tablename__='stores'
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(80))
    items=db.relationship('ItemModel',lazy='dynamic')
    def __init__(self,name):
        self.name=name

    def json(self):
        return {"name":self.name,
                "items":[item.json() for item in self.items.all()]
                }
    @classmethod
    def find_item_name(cls, name):

        print(name)
        return cls.query.filter_by(name=name).first() #select * from iterms where name=name

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()