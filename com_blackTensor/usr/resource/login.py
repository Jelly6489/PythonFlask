from flask import request, make_response
from flask_restful import Resource, reqparse
from flask import jsonify
import os
import json

from com_blackTensor.usr.model.user_dao import UserDao, ReviewDao
from com_blackTensor.usr.model.user_dfo import UserDfo
from com_blackTensor.usr.model.user_dto import UserDto, ReviewDto, UserVo

parser = reqparse.RequestParser() 

class Login(Resource):
    # print(f'[ User Login Resource Enter ]')
    @staticmethod
    def post():
        print('======login post======')
        print(f'parser ===> {parser}')

        parser.add_argument('email')
        parser.add_argument('password')

        args = parser.parse_args()
        print(f'args ===> {args}')

        user = UserVo()
        print(f'user : {user}')
        
        print(f'[ ID ] {args.email} \n [ Password ] {args.password}')
        user.email = args.email
        user.password = args.password

        print('아이디: ', user.email)
        print('비밀번호: ', user.password)

        data = UserDao.login(user)
        print(f'Login Result : {data}')

        # return data[0], 200
        # return data.json(), 200
        return jsonify([data.json])
