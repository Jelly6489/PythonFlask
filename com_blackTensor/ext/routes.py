import logging
from flask import Blueprint
from flask_restful import Api

from com_blackTensor.resources.covid.status.resource.status import CovidStatus
from com_blackTensor.resources.covid.borad.resources.covid_board import CovidBoard
from com_blackTensor.resources.news.covid.resources.covid_news import CovidNews
from com_blackTensor.resources.news.economy.resources.economy_news import EconomyNews
from com_blackTensor.resources.predict.resource.predict import Predict, PredictDate

from com_blackTensor.resources.emo.resource.emotion import Emotion, StockNews
from com_blackTensor.resources.fin.resource.finance import Finance
from com_blackTensor.resources.sto.resource.stock import Stock
from com_blackTensor.resources.exc.resource.exchange import Exchange, ExchangeData
from com_blackTensor.usr.resource.user import User, Users
from com_blackTensor.usr.resource.review import Review, Reviews
from com_blackTensor.usr.resource.login import Login

covid = Blueprint('covidStatus', __name__, url_prefix='/api/status/covid')
board = Blueprint('covidBoard', __name__, url_prefix='/api/board/covid')

covid_news = Blueprint('CovidNews', __name__, url_prefix='/api/news/covid')
economy_news = Blueprint('EconomyNews', __name__, url_prefix='/api/news/economy')

fredict = Blueprint('Fredict', __name__, url_prefix='/api/pred')
fredict_date = Blueprint('FredictDate', __name__, url_prefix='/api/predDate')

stock = Blueprint("stock", __name__, url_prefix='/api/stock/stock')
finance = Blueprint('finance', __name__, url_prefix='/api/stock/finance')
emotion = Blueprint('emotion', __name__, url_prefix='/api/stock/emotion')
stock_news = Blueprint('stock_news', __name__, url_prefix='/api/stock/mainNews')
exchange = Blueprint('exchange', __name__, url_prefix='/api/stock/exchange')
exchange_data = Blueprint('exchange_data', __name__, url_prefix='/api/stock/exchangeData')
user = Blueprint('user', __name__, url_prefix='/api/access')
login = Blueprint('user', __name__, url_prefix='/api/login')
review = Blueprint('review', __name__, url_prefix='/api/mypage')

api = Api(covid)
api = Api(covid_news)
api = Api(board)
api = Api(economy_news)
api = Api(fredict)
api = Api(fredict_date)

api = Api(stock)
api = Api(finance)
api = Api(emotion)
api = Api(stock_news)
api = Api(exchange)
api = Api(exchange_data)
api = Api(user)
api = Api(login)
api = Api(review)

def initialize_route(api):
    api.add_resource(CovidStatus, '/api/status/covid')
    api.add_resource(CovidNews, '/api/news/covid')
    api.add_resource(CovidBoard, '/api/board/covid')
    api.add_resource(EconomyNews, '/api/news/economy')
    api.add_resource(Predict, '/api/pred/<string:stockName>')
    api.add_resource(PredictDate, '/api/predDate/<string:stockName>/<string:date>')

    api.add_resource(Stock, f'/api/stock/stock/<keyword>')
    api.add_resource(Finance, f'/api/stock/finance/<keyword>')
    api.add_resource(Emotion, f'/api/stock/emotion/<keyword>')
    api.add_resource(StockNews, f'/api/stock/mainNews/<keyword>')
    api.add_resource(Exchange, '/api/stock/exchange')
    api.add_resource(ExchangeData, '/api/stock/exchange_data/<keyword>')
    api.add_resource(User, '/api/access', '/api/access/<user_id>')
    api.add_resource(Login, '/api/login')
    api.add_resource(Review, '/api/mypage', '/api/mypage/<name>')

@covid.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during covid request. %s' % str(e))
    return 'An internal error occurred.', 500

@covid_news.errorhandler(500)
def frequency_api_error(e):
    logging.exception('An error occurred during frequency request. %s' % str(e))
    return 'An internal error occurred.', 500

@board.errorhandler(500)
def board_api_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500

@economy_news.errorhandler(500)
def economy_news_api_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500

@fredict.errorhandler(500)
def fredict_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500

@fredict_date.errorhandler(500)
def fredict_date_date_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500

@stock.errorhandler(500)
def stock_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@finance.errorhandler(500)
def finance_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@emotion.errorhandler(500)
def emotion_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@stock_news.errorhandler(500)
def stock_news_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@exchange_data.errorhandler(500)
def exchange_data_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@exchange.errorhandler(500)
def exchange_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@user.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@login.errorhandler(500)
def review_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500