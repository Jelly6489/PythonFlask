from com_blacktensor.ext.db import db
from flask_restful import Resource
import csv
import pandas as pd
from sqlalchemy import create_engine

# ============================================================
# ==================                     =====================
# ==================         KDD         =====================
# ==================                     =====================
# ============================================================
class StockKdd(object):
    def __init__(self, code_df, code, url):
        # 삼성전자의 일자 데이터 url
        self.item_name=['셀트리온', '삼성전자', '하나투어']
        self.code_df = code_df
        self.url = url
        self.code = code

    def get_code(self, code_df):
        # 한국거래소(krx)
        self.code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13',header=0)[0]
        
        # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해둠
        code_df.종목코드 = self.code_df.종목코드.map('{:06d}'.format)

        # 회사명과 종목코드 필요 -> 그 이외에 필요 없는 column 제외
        code_df = self.code_df[['회사명', '종목코드']]

        # 한글로된 컬럼명을 영어로 변환
        code_df = self.code_df.rename(columns={'회사명' : 'name', '종목코드' : 'code'})
        code_df.head()
        print(code_df.head())

    # https://finance.naver.com/item/sise.nhn?code=005930(삼성전자)
    def get_url(self, item_name, code_df, code):
        self.code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False).strip()
        # code = code.strip()

        url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)

        print("요청 URL = {}".format(url))
        
        # return url

    def get_data(self, get_url, item_name, code_df):
        for i in item_name:
            print('\n'+i)
            url = get_url(i, code_df)

        # 일자 데이터를 담을 df라는 DataFrame 정의
        self.df = pd.DataFrame()

        # 1페이지에서 15페이지의 데이터만 가져오기(약 6개월치)
        for page in range(1, 16): 
            pg_url = '{url}&page={page}'.format(url=url, page=page) 
            df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)

        # df.dropna()를 이용해 결측값 있는 행 제거
        df = df.dropna()

        # df.drop()을 이용해 columns 삭제
        df = df.drop(columns= {'전일비', '고가', '저가'})

        # 한글 -> 영어
        df = df.rename(columns= {
            '날짜': 'date', '종가': 'close', '시가': 'open', '거래량': 'volume'})

        # 데이터 타입 int 변환
        df[['close', 'open', 'volume']] = df[['close', 'open', 'volume']].astype(int)

        # date를 date type 변환
        df['date'] = pd.to_datetime(df['date'])

        # date 기준으로 내림차순 sort
        df = df.sort_values(by=['date'], ascending=False)
        
        df.head()
        print('-------------------- head -------------------')
        print(df.head())
        print('\n-------------------- 전체 -------------------')
        print(df)
        
        # csv file 저장
        df.to_csv(i + '.csv', mode = 'a', header = False)
        
# ============================================================
# ==================                     =====================
# ==================    Preprocessing    =====================
# ==================                     =====================
# ============================================================
class StockDf(object):
    ...

# ============================================================
# ==================                     =====================
# ==================       Modeling      =====================
# ==================                     =====================
# ============================================================
class StockDto(db.Model):
    ...

class StockDao(StockDto):
    ...

class StockVo(object):
    ...

class StockTf(object):
    ...

class StockAi(object):
    ...

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class Stock(Resource):
    ...



# class StockCrow():
#     def __init__(self, code_df, code, url):
#         # 삼성전자의 일자 데이터 url
#         self.item_name=['셀트리온', '삼성전자', '하나투어']
#         self.code_df = code_df
#         self.url = url
#         self.code = code

#     def get_code(self, code_df):
#         # 한국거래소(krx)
#         self.code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13',header=0)[0]
        
#         # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해둠
#         code_df.종목코드 = self.code_df.종목코드.map('{:06d}'.format)

#         # 회사명과 종목코드 필요 -> 그 이외에 필요 없는 column 제외
#         code_df = self.code_df[['회사명', '종목코드']]

#         # 한글로된 컬럼명을 영어로 변환
#         code_df = self.code_df.rename(columns={'회사명' : 'name', '종목코드' : 'code'})
#         code_df.head()
#         print(code_df.head())

#     # https://finance.naver.com/item/sise.nhn?code=005930(삼성전자)
#     def get_url(self, item_name, code_df, code):
#         self.code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False).strip()
#         # code = code.strip()

#         url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)

#         print("요청 URL = {}".format(url))
        
#         # return url

#     def get_data(self, get_url, item_name, code_df):
#         for i in item_name:
#             print('\n'+i)
#             url = get_url(i, code_df)

#         # 일자 데이터를 담을 df라는 DataFrame 정의
#         self.df = pd.DataFrame()

#         # 1페이지에서 15페이지의 데이터만 가져오기(약 6개월치)
#         for page in range(1, 16): 
#             pg_url = '{url}&page={page}'.format(url=url, page=page) 
#             df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)

#         # df.dropna()를 이용해 결측값 있는 행 제거
#         df = df.dropna()

#         # df.drop()을 이용해 columns 삭제
#         df = df.drop(columns= {'전일비', '고가', '저가'})

#         # 한글 -> 영어
#         df = df.rename(columns= {
#             '날짜': 'date', '종가': 'close', '시가': 'open', '거래량': 'volume'})

#         # 데이터 타입 int 변환
#         df[['close', 'open', 'volume']] = df[['close', 'open', 'volume']].astype(int)

#         # date를 date type 변환
#         df['date'] = pd.to_datetime(df['date'])

#         # date 기준으로 내림차순 sort
#         df = df.sort_values(by=['date'], ascending=False)
        
#         df.head()
#         print('-------------------- head -------------------')
#         print(df.head())
#         print('\n-------------------- 전체 -------------------')
#         print(df)
        
#         # csv file 저장
#         df.to_csv(i + '.csv', mode = 'a', header = False)


# # class StockDto(db.Model):
# #     __tablename__ = 'code'
# #     __table_args__={'mysql_collate' : 'utf8_general_ci'}

# #     date : str = db.Column(db.String(10), primary_key = True, index = True)
# #     close : int = db.Column(db.Int)
# #     open : int = db.Column(db.Int)
# #     volume : int = db.Column(db.Integer)

# #     def __init__(self, date, close, open, volume):
# #         self.date = date
# #         self.close = close
# #         self.open = open
# #         self.volume = volume
    
# #     def __repr__(self):
# #         return f'Stock(date={self.date}, close={self.close}\
# #             , open={self.open}, volume={self.volume})'

# # class StockVo:
# #     date : str = ''
# #     close : int = 0
# #     open : int = 0
# #     volume : int = 0