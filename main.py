from flask import Flask
from flask_restful import Api
from com_blackTensor.ext.db import url, db
from com_blackTensor.ext.routes import initialize_route
from flask_cors import CORS

import datetime
import time
import threading

from com_blackTensor.util.checker import Checker 
from com_blackTensor.util.file_hander import FileHandler as handler

from com_blackTensor.resources.covid.status.model.status_kdd import CovidStatusKdd
from com_blackTensor.resources.covid.status.model.status_df import CovidStatusDf
from com_blackTensor.resources.covid.status.model.status_dao import CovidStatusDao
from com_blackTensor.resources.covid.status.model.status_dto import CovidStatusDto
from com_blackTensor.resources.news.covid.model.covid_news_dto import CovidNewsDto, CovidExtractionWordDto
from com_blackTensor.resources.news.economy.model.economy_dto import EconomyNewsDto, EconomyExtractionWordDto

# =============================== Emotion ===============================
from com_blackTensor.resources.emo.model.emotion_kdd import keyword
from com_blackTensor.resources.emo.model.emotion_dao import EmotionDao, StockNewsDao
from com_blackTensor.resources.emo.model.emotion_dfo import EmotionDfo
from com_blackTensor.resources.emo.model.emotion_kdd import EmotionKdd
from com_blackTensor.resources.emo.model.emotion_dto import EmotionDto, StockNewsDto
from com_blackTensor.resources.emo.model import emotion_dfo
# =============================== Finance ===============================
from com_blackTensor.resources.fin.model.finance_dao import FinanceDao
from com_blackTensor.resources.fin.model.finance_dfo import FinanceDfo
from com_blackTensor.resources.fin.model.finance_dto import FinanceDto
from com_blackTensor.resources.fin.model.finance_kdd import FinanceKdd
# =============================== Stock ===============================
from com_blackTensor.resources.sto.model.stock_dao import StockDao
from com_blackTensor.resources.sto.model.stock_dfo import StockDfo
from com_blackTensor.resources.sto.model.stock_dto import StockDto
from com_blackTensor.resources.sto.model.stock_kdd import StockKdd
# =============================== Exchange ===============================
from com_blackTensor.resources.exc.model.exchange_kdd import ExchangeKdd
from com_blackTensor.resources.exc.model.exchange_dfo import ExchangeDfo
from com_blackTensor.resources.exc.model.exchange_dao import ExchangeDao
from com_blackTensor.resources.exc.model.exchange_dto import ExchangeDto
from com_blackTensor.resources.exc.model.exchange_ai import ExchangeAi
# =============================== User ===============================
from com_blackTensor.usr.model.user_dao import UserDao, ReviewDao
from com_blackTensor.usr.model.user_dfo import UserDfo
from com_blackTensor.usr.model.user_dto import UserDto, ReviewDto

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api = Api(app)



if __name__ == '__main__':
    # keyword = ["삼성전자", "셀트리온", "하나투어"]
    # for k, m in enumerate(keyword):
    # print(m)
    code_df = FinanceKdd()
    # EmotionDfo.data_pro(0, keyword)
    EmotionDfo.data_pro(0, keyword)
    FinanceKdd.get_finance(0, keyword, code_df)
    ExchangeKdd.market_index_kdd(0)
    ExchangeDfo.get_ex_df(0)

    # FinanceDfo.fina_pro(keyword)

with app.app_context():
    db.create_all()

    status_count = CovidStatusDao.count()
    emotion_count = EmotionDao.count()
    stock_new_count = StockNewsDao.count()
    stock_count = StockDao.count()
    finance_count = FinanceDao.count()
    exchange_count = ExchangeDao.count()
    user_count = UserDao.count()
    review_count = ReviewDao.count()

    if status_count == 0:
        endDate = datetime.date.today().strftime('%Y%m%d')
        datas = CovidStatusKdd().get_covid19_status(endDate)

        if len(datas) > 0:
            if not Checker.check_folder_path('./csv'):
                handler.crete_folder('./csv')
            
            keys = list(datas[0].keys())
            handler.save_to_csv('./csv/result_covid19_status.csv', datas, keys, 'utf-8-sig')

            df = CovidStatusDf(keys).get_dataframe(datas)
            CovidStatusDao.save_data_bulk(df)

    print(f'***** Emotion Total Count is {emotion_count} *****')
    if emotion_count[0] == 0:
        EmotionDao.bulk()
    else :
        EmotionDao.find_keyword(keyword)

    print(f'***** StockNews Total Count is {stock_new_count} *****')
    if stock_new_count[0] == 0:
        StockNewsDao.bulk()
    else :
        StockNewsDao.find_keyword(keyword)

    print(f'***** Stock Total Count is {stock_count} *****')
    if stock_count[0] == 0:
        StockDao.bulk()
    else :
        StockDao.find_keyword(keyword)

    print(f'***** Finance Total Count is {finance_count} *****')
    if finance_count[0] == 0:
        FinanceDao.bulk()
    else :
        FinanceDao.find_keyword(keyword)

    print(f'***** Exchange Total Count is {exchange_count} *****')
    if exchange_count[0] == 0:
        ExchangeDao.bulk()

    print(f'***** Exchange Total Count is {user_count} *****')
    if user_count[0] == 0:
        UserDao.bulk()
    else:
        print("Users Data exists...")

    print(f'***** Exchange Total Count is {review_count} *****')
    if review_count[0] == 0:
        ReviewDao.bulk()
    else:
        print("Reivews Data exists...")
initialize_route(api)