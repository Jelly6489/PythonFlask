import csv
import pandas as pd
from com_blackTensor.ext.db import db, openSeesion, engine
from sqlalchemy import func
from com_blackTensor.resources.emo.model.emotion_kdd import keyword, key1, key2, key3
from com_blackTensor.util.file_hander import FileHandler as handler
from datetime import datetime
from dateutil.relativedelta import relativedelta

# # # ============================================================
# # # ==================                     =====================
# # # ==================         KDD         =====================
# # # ==================                     =====================
# # # ============================================================
class StockKdd(object):
    # keyword = input("검색어 입력: ")

    current = datetime.today()
    pre_current = datetime.now()-relativedelta(years=5)
    dx = current.strftime("%Y-%m-%d")
    dy = pre_current.strftime("%Y-%m-%d")

    code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13',header=0)[0]
    #
    # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해둠
    code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

    # 회사명과 종목코드 필요 -> 그 이외에 필요 없는 column 제외
    code_df = code_df[['회사명', '종목코드']]

    # 한글로된 컬럼명을 영어로 변환
    code_df = code_df.rename(columns={'회사명' : 'name', '종목코드' : 'code'})
    code_df.head()
    print('----------------stock------------------')
    print(code_df.head())

    # https://finance.naver.com/item/sise.nhn?code=005930(삼성전자)
    def get_url(self, keyword, code_df):
        code = code_df.query("name=='{}'".format(keyword))['code'].to_string(index=False)
        code = code.strip()

        url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
        
        print("요청 URL = {}".format(url))
        return url

    for k, m in enumerate(keyword):
        if m == key1:
            url = get_url(0, key1, code_df)
        if m == key2:
            url = get_url(0, key2, code_df)
        if m == key3:
            url = get_url(0, key3, code_df)

        # url = get_url(0, keyword, code_df)

        df = pd.DataFrame()

        # for page in range(1, 64): 
        for page in range(1, 125): 
            pg_url = '{url}&page={page}'.format(url=url, page=page) 
            df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)

        df = df.dropna()

        # df = df.drop(columns= {'전일비', '시가', '고가', '저가'})
        df = df.drop(columns= {'전일비'})

        # print(df.head())
        print(df)

        df = df.rename(columns= {
            '날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open',
            '고가': 'high', '저가': 'low', '거래량': 'volume'
            })

        # df.drop(['diff', 'open', 'high', 'low'], axis=1, inplace=True)

        # 데이터 타입 int 변환
        # df[['close', 'volume']] \
        #     = df[['close', 'volume']].astype(int)

        df[['close', 'open', 'high', 'low', 'volume']] \
            = df[['close', 'open', 'high', 'low', 'volume']].astype(float)

        # df.drop(['diff', 'open', 'high', 'low'], axis=0, inplace=True)

        # date를 date type 변환
        mask = (df['date'] > dy) & (df['date'] <= dx)
        filterrd_df = df.loc[mask]
        print('==============filterrd_df===============')
        print(filterrd_df)

        df['date'] = pd.to_datetime(df['date'])

        # date 기준으로 내림차순 sort
        # df = df.sort_values(by=['date'], ascending=False)
        df = df.sort_values(by=['date'], ascending=True)

        df.loc[:, 'keyword'] = m

        # df.head()
        print('-------------------- head -------------------')
        print(df.head())
        print('\n-------------------- 전체 -------------------')
        print(df)

        # csv file 저장
        # df.to_csv(keyword + '_data.csv', encoding='utf-8-sig')
        df.to_csv('./csv/{}_data.csv'.format(m), encoding='utf-8-sig')

