from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
# import sqlite3
from Modules.item import  ItemModel

class Items(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('price',
                       type=float,
                       required=True,
                       help="this fild is Required"
                       )

    parse.add_argument('store_id',
                       type=int,
                       required=True,
                       help="this fild is Required, every item need a store id "
                       )
    @jwt_required()
    def get(self, name):

        item = ItemModel.find_item_name(name)
        if item:
            return item.json()
        return {"messange": "item not Found"}



    def post(self, name):
        if ItemModel.find_item_name(name):
            return {"message": "An Iteam with name '{}' already exist ".format(name)}, 400

        else:
            data = Items.parse.parse_args()  # if header is not specified
            # also can be used as silent=True

            item = ItemModel(name,**data)

            try:
                item.save_to_db()
            except:
                return {"messange": "error ocurred while Inserting "}, 500
            return item.json(), 201

        # creating status


    def delete(self, name):

        item=ItemModel.find_item_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'item deleted'}
        else:
            return {"error ":"No item named after this "}
    def put(self, name):

        data = Items.parse.parse_args()
        item=ItemModel.find_item_name(name)
        if item:
            item=ItemModel(name,**data)
        else:
            item.price=data['price']
        item.save_to_db()
        return  item.json()




class IteamList(Resource):
    def get(self):
        # return {
        #     "items":  [item.json() for item in  ItemModel.query.all()]
        # }

        return {"items":list(map(lambda x:x.json() , ItemModel.query.all()))}