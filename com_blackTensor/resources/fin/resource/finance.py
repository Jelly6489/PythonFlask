from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify

from com_blackTensor.resources.fin.model.finance_dao import FinanceDao
from com_blackTensor.resources.fin.model.finance_dfo import FinanceDfo
from com_blackTensor.resources.fin.model.finance_kdd import FinanceKdd
from com_blackTensor.resources.fin.model.finance_dto import FinanceVo

from com_blackTensor.resources.emo.model.emotion_kdd import keyword

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class Finance(Resource):
    def __init__(self):
        self.dao = FinanceDao()

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
            stockNews = FinanceDao.find_by_keyword(keyword)
            print('=============확인==============')
            if stockNews:
                return jsonify([item.json for item in stockNews])
        except Exception as e:
            print(e)
            return {'error': 'Emotion not found'}, 404