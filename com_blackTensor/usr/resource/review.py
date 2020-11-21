from flask import request, make_response
from flask_restful import Resource, reqparse
from flask import jsonify
import os
import json

from com_blackTensor.usr.model.user_dao import UserDao, ReviewDao
from com_blackTensor.usr.model.user_dfo import UserDfo
from com_blackTensor.usr.model.user_dto import UserDto, ReviewDto

parser = reqparse.RequestParser() 

class Review(Resource):

    @staticmethod
    def post():
        print('====== review post 요청 받음 ======')
        print(f'[Review Signup Resource Enter]')
        args = parser.parse_args()
        print('type(args): ', type(args))
        print('args: ', args)

        body = request.get_json()
        print('type(body): ', type(body))
        print('body: ', body)
        if len(body) == 0:
            return 'No parameter'

        # body = body['reviewInfo']
        # print('after body : ', body)

        body_str = ''
        for key in body.keys():
            body_str += 'key: {}, value: {}<br>'.format(key, body[key])

        # create 구현
        review = ReviewDto(**body)
        ReviewDao.save(review)
        name = review.name

        return {'message': 'SUCCESS', 'email': str(name)}, 200

    @staticmethod
    def get(name: str):
        print('===========name=============')
        print(name)
        try:
            print(f'Review Name is {name}')
            review = ReviewDao.find_by_name(name)
            print(review)
            if review:
                return jsonify([review.json])
        except Exception as e:
            print(e)
            return {'error': 'Review not found'}, 404

    @staticmethod
    def delete():
        print(f'[ Review Delete Resource Enter ] ')
        args = parser.parse_args()
        print(f'Review {args["name"]} deleted')
        return {'code' : 0, 'message' : 'SUCCESS'}, 200 

class Reviews(Resource):
            
    @staticmethod
    def post():
        print(f'[ Review Bulk Resource Enter ] ')
        ReviewDao.bulk()

    @staticmethod
    def get():
        print(f'[ Review List Resource Enter ]')
        data = ReviewDao.find_all()
        return jsonify([item.json for item in data])