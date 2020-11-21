from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
import json

from com_blackTensor.resources.emo.model.emotion_dao import EmotionDao, StockNewsDao
from com_blackTensor.resources.emo.model.emotion_dfo import EmotionDfo
from com_blackTensor.resources.emo.model.emotion_kdd import EmotionKdd
from com_blackTensor.resources.emo.model.emotion_dto import EmotionVo
from com_blackTensor.resources.emo.model.emotion_dto import EmotionDto

from com_blackTensor.resources.emo.model.emotion_kdd import keyword

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class Emotion(Resource):
    def __init__(self):
        self.dao = EmotionDao()

    @staticmethod
    def post():
        print(f'[ Emotion Signup Resource Enter ] ')
        body = request.get_json()
        emotion = EmotionDto(**body)
        EmotionDao.save(emotion)
        
        return {'emotion': str(emotion)}, 200

    # def get(self):
    #     result = EmotionDao().find_all()
    #     return jsonify([item.json for item in result])
    @staticmethod
    def get(keyword: str):
        """
        유저 아이디를 받아와 해당 유저 객채를 리턴한다
        Parameter: User ID 를 받아온다
        return: 해당 아이디 유저 객체
        """
        print('===========Emotion=============')
        print(keyword)
        try:
            print(f'Emotion is {keyword}')
            emotion = EmotionDao.find_by_keyword(keyword)
            print('=============확인==============')
            if emotion:
                # return jsonify([emotion.json])
                return jsonify([item.json for item in emotion])
        except Exception as e:
            print(e)
            return {'error': 'Emotion not found'}, 404

class StockNews(Resource):
    def __init__(self):
        self.dao = StockNewsDao()

    # def get(self):
    #     result = self.dao.find_all()
    #     return jsonify([item.json for item in result])
    @staticmethod
    def get(keyword: str):
        """
        유저 아이디를 받아와 해당 유저 객채를 리턴한다
        Parameter: User ID 를 받아온다
        return: 해당 아이디 유저 객체
        """
        print('===========Emotion=============')
        print(keyword)
        try:
            print(f'Emotion is {keyword}')
            stockNews = StockNewsDao.find_by_keyword(keyword)
            print('=============확인==============')
            if stockNews:
                return jsonify([item.json for item in stockNews])
        except Exception as e:
            print(e)
            return {'error': 'Emotion not found'}, 404