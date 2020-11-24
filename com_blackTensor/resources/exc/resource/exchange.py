import requests
import pandas as pd
import codecs
import numpy as np
import re
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
from com_blackTensor.util.checker import Checker

from com_blackTensor.resources.exc.model.exchange_kdd import ExchangeKdd
from com_blackTensor.resources.exc.model.exchange_dao import ExchangeDao
from com_blackTensor.resources.exc.model.exchange_dfo import ExchangeDfo
from com_blackTensor.resources.exc.model.exchange_dto import ExchangeDto
from com_blackTensor.resources.emo.model.emotion_kdd import keyword, key1, key2, key3
from com_blackTensor.resources.sto.model.stock_dto import StockDto
from com_blackTensor.resources.sto.model.stock_dao import StockDao

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class Exchange(Resource):
    def __init__(self):
        self.dao = ExchangeDao()

    def get(self):
        print('================Exchange1================')
        result = self.dao.find_all()

        print('================Exchange2================')
        # url = 'http://192.168.0.10:8080/api/stock/lstm_usd'
        # files = {'file': open('./ai_data/{}_LSTM_USD.png'.format(keyword), 'rb')}
        # r = requests.post(url, files=files)
        # if keyword == "삼성전자":
        #     return {
        #         'lstm_usd': Checker.get_abs_path('./ai_data/{}_LSTM_USD.png'.format(keyword)),
        #         'lstm_jpy': Checker.get_abs_path('./ai_data/{}_LSTM_JPY.png'.format(keyword)),
        #         'lstm_eur': Checker.get_abs_path('./ai_data/{}_LSTM_EUR.png'.format(keyword)),
        #         'lstm_cny': Checker.get_abs_path('./ai_data/{}_LSTM_CNY.png'.format(keyword)),
        #         'lstm_usd_cny': Checker.get_abs_path('./ai_data/{}_LSTM_USD_CNY.png'.format(keyword)),
        #         'lstm_all': Checker.get_abs_path('./ai_data/{}_LSTM_All.png'.format(keyword))
        #         }
        # if keyword == "셀트리온":
        #     return {
        #         'lstm_usd': Checker.get_abs_path('./ai_data/{}_LSTM_USD.png'.format(keyword)),
        #         'lstm_jpy': Checker.get_abs_path('./ai_data/{}_LSTM_JPY.png'.format(keyword)),
        #         'lstm_eur': Checker.get_abs_path('./ai_data/{}_LSTM_EUR.png'.format(keyword)),
        #         'lstm_cny': Checker.get_abs_path('./ai_data/{}_LSTM_CNY.png'.format(keyword)),
        #         'lstm_usd_cny': Checker.get_abs_path('./ai_data/{}_LSTM_USD_CNY.png'.format(keyword)),
        #         'lstm_all': Checker.get_abs_path('./ai_data/{}_LSTM_All.png'.format(keyword))
        #         }
        # if keyword == "하나투어":
        #     return {
        #         'lstm_usd': Checker.get_abs_path('./ai_data/{}_LSTM_USD.png'.format(keyword)),
        #         'lstm_jpy': Checker.get_abs_path('./ai_data/{}_LSTM_JPY.png'.format(keyword)),
        #         'lstm_eur': Checker.get_abs_path('./ai_data/{}_LSTM_EUR.png'.format(keyword)),
        #         'lstm_cny': Checker.get_abs_path('./ai_data/{}_LSTM_CNY.png'.format(keyword)),
        #         'lstm_usd_cny': Checker.get_abs_path('./ai_data/{}_LSTM_USD_CNY.png'.format(keyword)),
        #         'lstm_all': Checker.get_abs_path('./ai_data/{}_LSTM_All.png'.format(keyword))
        #         }
        return jsonify([item.json for item in result])

class ExchangeData(Resource):
    @staticmethod
    def get(keyword: str):
        print('========ExchangeData=========')
        print(keyword)
        exchange = ExchangeDao.find_by_keyword(keyword)
        print('=============== ExchangeData Test1 ================')
        try:
            print('=============== ExchangeData Test2 ================')
            if keyword == "삼성전자":
                print('=============== ExchangeData Test3 ================')
                return {
                    'lstm_usd': Checker.get_abs_path('./ai_data/{}_LSTM_USD.png'.format(keyword)),
                    'lstm_jpy': Checker.get_abs_path('./ai_data/{}_LSTM_JPY.png'.format(keyword)),
                    'lstm_eur': Checker.get_abs_path('./ai_data/{}_LSTM_EUR.png'.format(keyword)),
                    'lstm_cny': Checker.get_abs_path('./ai_data/{}_LSTM_CNY.png'.format(keyword)),
                    'lstm_usd_cny': Checker.get_abs_path('./ai_data/{}_LSTM_USD_CNY.png'.format(keyword)),
                    'lstm_all': Checker.get_abs_path('./ai_data/{}_LSTM_All.png'.format(keyword))
                }
            if keyword == "셀트리온":
                print('=============== ExchangeData Test4 ================')
                return {
                    'lstm_usd': Checker.get_abs_path('./ai_data/{}_LSTM_USD.png'.format(keyword)),
                    'lstm_jpy': Checker.get_abs_path('./ai_data/{}_LSTM_JPY.png'.format(keyword)),
                    'lstm_eur': Checker.get_abs_path('./ai_data/{}_LSTM_EUR.png'.format(keyword)),
                    'lstm_cny': Checker.get_abs_path('./ai_data/{}_LSTM_CNY.png'.format(keyword)),
                    'lstm_usd_cny': Checker.get_abs_path('./ai_data/{}_LSTM_USD_CNY.png'.format(keyword)),
                    'lstm_all': Checker.get_abs_path('./ai_data/{}_LSTM_All.png'.format(keyword))
                }
            if keyword == "하나투어":
                print('=============== ExchangeData Test5 ================')
                # return {
                #     'lstm_usd': Checker.get_abs_path('./ai_data/{}_LSTM_USD.png'.format(m))
                # }
                return {
                    'lstm_usd': Checker.get_abs_path('./ai_data/{}_LSTM_USD.png'.format(keyword)),
                    'lstm_jpy': Checker.get_abs_path('./ai_data/{}_LSTM_JPY.png'.format(keyword)),
                    'lstm_eur': Checker.get_abs_path('./ai_data/{}_LSTM_EUR.png'.format(keyword)),
                    'lstm_cny': Checker.get_abs_path('./ai_data/{}_LSTM_CNY.png'.format(keyword)),
                    'lstm_usd_cny': Checker.get_abs_path('./ai_data/{}_LSTM_USD_CNY.png'.format(keyword)),
                    'lstm_all': Checker.get_abs_path('./ai_data/{}_LSTM_All.png'.format(keyword))
                }
        except Exception as e:
            print(e)
            return {'error': 'ExchangeData not found'}, 404
