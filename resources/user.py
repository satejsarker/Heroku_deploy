import  sqlite3
from flask_restful import  Resource, reqparse
from Modules.user import UserModel


class UserResgister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="this fild is required ")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="this fild cant be blank "
                        )

    def post(self):
        data=UserResgister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return  {'Message': "User name already Exist"},400
        user=UserModel(**data)
        user.save_to_db()
        return {'message':"new User created "},201
