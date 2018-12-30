from flask import Flask
from flask_restful import  Api
from flask_jwt import  JWT
from Security import  authenticate,identity
from resources.user import  UserResgister
from resources.item import Items , IteamList
from resources.store import Store,  StoreList
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
# app.config['SQLALCHEMY_DATABASE_URI']="mysql://satej:satej@localhost:3306/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='satej@)((!!!klnvlknsdfiasdasdmnnjan$$%'

@app.before_first_request
def create_table():
    db.create_all()

api=Api(app)
jwt=JWT(app,authenticate,identity)

##demo in maemory data
#Route
db.init_app(app)
api.add_resource(Items,'/iteam/<string:name>')
api.add_resource(IteamList,'/iteams')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/storelist')
api.add_resource(UserResgister,'/register')
if __name__ == '__main__':
    from db import  db
    db.init_app(app)
    app.run(port=5000)
