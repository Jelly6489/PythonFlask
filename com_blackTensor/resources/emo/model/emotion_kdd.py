import requests
import pandas as pd
import codecs
import numpy as np
import re
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter
from flask_restful import Resource, reqparse
# from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
import json
from datetime import datetime
# from main import keyword

from sqlalchemy import Column, Integer, String, Date
# import time
# import multiprocessing
# ============================================================
# ==================                     =====================
# ==================         KDD         =====================
# ==================                     =====================
# ============================================================
# ====================================================== 동적 ==============================================================
# info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+"시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
# maxpage = int(input("최대 크롤링할 페이지 수 입력하시오: "))
# keyword = input("검색어 입력: ")
# order = input("뉴스 검색 방식 입력(관련도순=0 최신순=1 오래된순=2): ") #관련도순=0 최신순=1 오래된순=2
# s_date = input("시작날짜 입력(예: 2020.07.20):")
# e_date = input("끝날짜 입력(예: 2020.10.30):")
# info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+"시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
# =======================================================================================================================
keyword = ["삼성전자", "셀트리온", "하나투어"]
key1 = "삼성전자"
key2 = "셀트리온"
key3 = "하나투어"
maxpage = 20
order = "0"
s_date = "2020.01.01"
e_date = datetime.today().strftime("%Y.%m.%d")
date_text = []
# ### HeadLine
class EmotionKdd(object):
    def __init__(self):
        self.info_main = info_main
        self.maxpage = maxpage
        # self.keyword = keyword
        self.order = order
        self.s_date = s_date
        self.e_date = e_date

    def naver_news(self, maxpage, keyword, order, s_date, e_date):
        results = []
        data_results = []
        test_date = []
        
        for i in range(maxpage)[1:]:
            url = r'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort={}&photo=0&\
                    field=0&reporter_article=&pd=3&ds={}&de={}&docid=&nso=so:da,p:from20201028to20201030,\
                    a:all&mynews=0&start={}&refresh_start=0'.format(keyword, order, s_date, e_date, 10*(i-1)+1)
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            if i % 100 == 0:
                print(i,"번째 크롤링")

            title_list = soup.find_all('a', class_ = 'news_tit')

            for tag in title_list:
                results.append(tag.text)

### ------------------------------------------------------
            date_lists = soup.select('span.info')

            for date_list in date_lists:
                test = date_list.text

            # print("날짜 데이터!!!!: ", test)
            try:
                pattern = '\d+.(\d+).(\d+).'
                r = re.compile(pattern)
                match = r.search(test)#.group(0) # 2018.11.05.
                # date_text.append(match)
                test_date.append(test)
            except AttributeError:

                pattern = '\w* (\d\w*)'

                r = re.compile(pattern)
                match = r.search(test)#.group(1)
                #print(match)
                # date_text.append(match)
                test_date.append(test)
            
        # print("크롤링 날짜!! :", date_text)
        # print("날짜 데이터!!!!: ", test_date)
        return results

        '''
                                    title keyword
    0             삼성전자, 수원·화성 공장서 잇따라 확진    삼성전자
    1  '노조와해 시도' 강경훈 삼성 부사장 2심도 징역 1년4개월    삼성전자
    2     [속보] 삼성전자 수원사업장 직원 6명 코로나19 확진    삼성전자
    3               삼성이 개발 중인 롤러블폰의 모습은?    삼성전자
    4     대기업 잉여현금흐름 1년 새 17조 증가…삼성전자 1위    삼성전자
        '''
### ------------------------------------------------------
            

            # #날짜 추출
            # date_lists = soup.select('.info_group')
            # for date_list in date_lists:
            #     test=date_list.text
            #     DateCleansing(0, test)

        #     for tag in title_list:
        #         # results += tag.get_text()
        #         data_results.append(tag.text)
        #     new_date = {"date" : date_text}
        # return data_results

    # def DateCleansing(self, test):
    #     try:
    #         pattern = '\d+.(\d+).(\d+).'
    #         r = re.compile(pattern)
    #         match = r.search(test).group(0) # 2018.11.05.
    #         date_text.append(match)
    #     except AttributeError:

    #         pattern = '\w* (\d\w*)'

    #         r = re.compile(pattern)
    #         match = r.search(test).group(1)
    #         #print(match)
    #         date_text.append(match)
    
    # print("크롤링 날짜!! :",date_text)

    # result = naver_news(object, keyword, 1)
    # ===================================================================================
        # for k, m in enumerate(keyword):
        #     if m == "삼성전자":
        #         result = naver_news(object, maxpage, m, order, s_date, e_date)
        #         print(m)
        #         df = pd.DataFrame(result)
        #         # print(df)
        #         df.columns = ['title']
        #         df.loc[:, 'keyword'] = m
        #         print('--------EmotionKdd-----------')
        #         print(df.head())
        #         df.to_csv('./csv/{}.csv'.format(keyword), encoding='utf-8-sig')
        #     if m == "셀트리온":
        #         result = naver_news(object, maxpage, m, order, s_date, e_date)
        #         print(m)
        #         df = pd.DataFrame(result)
        #         # print(df)
        #         df.columns = ['title']
        #         df.loc[:, 'keyword'] = m
        #         print('--------EmotionKdd-----------')
        #         print(df.head())
        #         df.to_csv('./csv/{}.csv'.format(keyword), encoding='utf-8-sig')
        #     if m == "하나투어":
        #         result = naver_news(object, maxpage, m, order, s_date, e_date)
        #         print(m)
        #         df = pd.DataFrame(result)
        #         # print(df)
        #         df.columns = ['title']
        #         df.loc[:, 'keyword'] = m
        #         print('--------EmotionKdd-----------')
        #         print(df.head())
        #         print(type(df))
        #         df.to_csv('./csv/{}.csv'.format(keyword), encoding='utf-8-sig')

    # ===================================================================================
        # print(m)
    for k, m in enumerate(keyword):
        if m == key1:
            result = naver_news(object, maxpage, key1, order, s_date, e_date)
            df = pd.DataFrame(result)
            df.columns = ['title']
            df.loc[:, 'keyword'] = key1
            print('--------EmotionKdd-----------')
            print(df.head())
            df.to_csv('./csv/{}.csv'.format(key1), encoding='utf-8-sig')
        if m == key2:
            result = naver_news(object, maxpage, key2, order, s_date, e_date)
            df = pd.DataFrame(result)
            df.columns = ['title']
            df.loc[:, 'keyword'] = key2
            print('--------EmotionKdd-----------')
            print(df.head())
            df.to_csv('./csv/{}.csv'.format(key2), encoding='utf-8-sig')
        if m == key3:
            result = naver_news(object, maxpage, key3, order, s_date, e_date)
            df = pd.DataFrame(result)
            df.columns = ['title']
            df.loc[:, 'keyword'] = m
            print('--------EmotionKdd-----------')
            print(df.head())
            df.to_csv('./csv/{}.csv'.format(key3), encoding='utf-8-sig')

# if __name__ == '__main__':
#     for k, m in enumerate(keyword):
#         if m == "삼성전자":
#             result = EmotionKdd.naver_news(object, maxpage, m, order, s_date, e_date)
#             df = pd.DataFrame(result)
#             # print(df)
#             df.columns = ['title']
#             df.loc[:, 'keyword'] = m
#             print('--------EmotionKdd-----------')
#             print(df.head())
#             df.to_csv('./csv/{}.csv'.format(m), encoding='utf-8-sig')
#         if m == "셀트리온":
#             EmotionKdd.naver_news(object, maxpage, m, order, s_date, e_date)
#             result = EmotionKdd.naver_news(object, maxpage, m, order, s_date, e_date)
#             df = pd.DataFrame(result)
#             # print(df)
#             df.columns = ['title']
#             df.loc[:, 'keyword'] = m
#             print('--------EmotionKdd-----------')
#             print(df.head())
#             df.to_csv('./csv/{}.csv'.format(m), encoding='utf-8-sig')
#         if m == "하나투어":
#             EmotionKdd.naver_news(object, maxpage, m, order, s_date, e_date)
#             result = EmotionKdd.naver_news(object, maxpage, m, order, s_date, e_date)
#             df = pd.DataFrame(result)
#             # print(df)
#             df.columns = ['title']
#             df.loc[:, 'keyword'] = m
#             print('--------EmotionKdd-----------')
#             print(df.head())
#             df.to_csv('./csv/{}.csv'.format(m), encoding='utf-8-sig')
#         print(m)
'''
0   논어, 새로운 가르침에 겁내지 않으려면 그간의 가르침을 실행해야 한다!       
1  "전 세계 AI 전문가 모여라"…'삼성 AI 포럼 2020' 온라인 개최
2              비트코인 지갑서비스 사업자도 자금세탁방지 의무 부과
3                  [연합뉴스 이 시각 헤드라인] - 12:00
4   “이건희 회장의 ‘도전 DNA’ 계승… 판도 바꾸는 기업으로 진화하자”
'''