from flask_restful import  Resource
from Modules.store import StoreModel


class Store(Resource):
    def get(self,name):
        print("Hit by the route ")
        store=StoreModel.find_item_name(name)
        if store:
            print (store)
            return store.json()
        return {"message":"Store not Found"},404
    def post (self,name):
        if StoreModel.find_item_name(name):
            return {"message":"'{}' store is already there ".format(name)},400
        else:
            try:
                store=StoreModel(name)
                store.save_to_db()
            except:
                return {"message":"error occurred when creating a store "},500
            return  store.json(),201



    def delete(self,name):
        store= StoreModel.find_item_name(name)
        if store:
            print(store)
            store.delete_from_db()
        return {"message":"store deleted"}
class StoreList(Resource):
    def get(self):
        return {"store":[store.json() for store in StoreModel.query.all() ]}