# import sqlite3
from db import  db

class ItemModel(db.Model):
    __tablename__='items'
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float(precision=2))
    store_id=db.Column(db.INTEGER, db.ForeignKey('stores.id'))
    store=db.relationship('StoreModel')
    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id=store_id
    def json(self):
        return {"name":self.name,
                "price":self.price
                }
    @classmethod
    def find_item_name(cls, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # qurry = 'SELECT * FROM items where name=?'
        # result = cursor.execute(qurry, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return  cls(*row)
        print(name)
        return cls.query.filter_by(name=name).first() #select * from iterms where name=name

    def save_to_db(self):
        # print("hited the methods")
        # print("name:{} , price:{}".format(self.name, self.price))
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # qurry = 'insert into items values (?,?)'
        # cursor.execute(qurry, (self.name, self.price))
        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()