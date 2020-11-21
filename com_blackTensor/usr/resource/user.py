from flask import request, make_response
from flask_restful import Resource, reqparse
from flask import jsonify
import os
import json

from com_blackTensor.usr.model.user_dao import UserDao
from com_blackTensor.usr.model.user_dfo import UserDfo
from com_blackTensor.usr.model.user_dto import UserDto

parser = reqparse.RequestParser() 

class User(Resource):

    # @staticmethod
    # def post():
    #     print(f'[ User Signup Resource Enter ] ')
    #     body = request.get_json()
    #     user = UserDto(**body)
    #     UserDao.save(user)
    #     email = user.email
        
    #     return {'email': str(email)}, 200

    @staticmethod
    def post():
        print('====== user post 요청 받음 ======')
        print(f'[User Signup Resource Enter]')
        args = parser.parse_args()
        print('type(args): ', type(args))
        print('args: ', args)

        body = request.get_json()
        print('type(body): ', type(body))
        print('body: ', body)
        if len(body) == 0:
            return 'No parameter'

        body = body['userInfo']
        print('after body : ', body)

        body_str = ''
        for key in body.keys():
            body_str += 'key: {}, value: {}<br>'.format(key, body[key])

        # create 구현
        user = UserDto(**body)
        UserDao.save(user)
        email = user.email

        return {'message': 'SUCCESS', 'email': str(email)}, 200

    @staticmethod
    def get(email: str):
        """
        유저 아이디를 받아와 해당 유저 객채를 리턴한다
        Parameter: User ID 를 받아온다
        return: 해당 아이디 유저 객체
        """
        print('===========user_id=============')
        print(email)
        try:
            print(f'User ID is {email}')
            user = UserDao.find_by_id(email)
            
            if user:
                return jsonify([user.json])
        except Exception as e:
            print(e)
            return {'message': 'User not found'}, 404

    @staticmethod
    def delete():
        print(f'[ User Delete Resource Enter ] ')
        args = parser.parse_args()
        print(f'User {args["email"]} deleted')
        return {'code' : 0, 'message' : 'SUCCESS'}, 200 

class Users(Resource):
            
    @staticmethod
    def post():
        print(f'[ User Bulk Resource Enter ] ')
        UserDao.bulk()

    # @staticmethod
    # def get():
    #     print(f'[ User List Resource Enter ] ')
    #     data = UserDao.find_all()
    #     return json.dumps(data), 200

    @staticmethod
    def get():
        print(f'[ User List Resource Enter ]')
        data = UserDao.find_all()
        return jsonify([item.json for item in data])