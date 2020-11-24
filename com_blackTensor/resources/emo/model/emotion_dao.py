import requests
import pandas as pd
import codecs
import numpy as np
import re
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter
from com_blackTensor.ext.db import db, openSeesion
from sqlalchemy import func
import json
from flask import jsonify

from sqlalchemy import Column, Integer, String, Date
from com_blackTensor.resources.emo.model.emotion_kdd import EmotionKdd
from com_blackTensor.resources.emo.model.emotion_dto import EmotionDto, StockNewsDto
from com_blackTensor.resources.emo.model.emotion_dfo import EmotionDfo
from com_blackTensor.resources.emo.model.emotion_kdd import keyword, key1, key2, key3

# import time
# import multiprocessing


Session = openSeesion()
session = Session()

class EmotionDao(EmotionDto):
    @staticmethod
    def bulk():
        emotion_dfo = EmotionDfo()
        emotion = session.query(EmotionDto).filter(EmotionDto.keyword.like(f'%{keyword}%')).all()
        for k, m in enumerate(keyword):
            if m == key1:
                if emotion == []:
                    dfo = emotion_dfo.data_pro(key1)
                    session.bulk_insert_mappings(EmotionDto, dfo.to_dict(orient='records'))
                    session.commit()
                    session.close()
            if m == key2:
                if emotion == []:
                    dfo = emotion_dfo.data_pro(key2)
                    session.bulk_insert_mappings(EmotionDto, dfo.to_dict(orient='records'))
                    session.commit()
                    session.close()
            if m == key3:
                if emotion == []:
                    dfo = emotion_dfo.data_pro(key3)
                    session.bulk_insert_mappings(EmotionDto, dfo.to_dict(orient='records'))
                    session.commit()
                    session.close()

    @staticmethod
    def save(emotion):
        session.add(emotion)
        session.commit()

    @classmethod
    def update(cls, emotion):
        emotion = session.query(cls).filter(cls.keyword == keyword).first()\
                .update({cls.no : emotion['no'],\
                cls.positive:emotion['tag'],\
                cls.pos_count:emotion['weight'],\
                cls.negative:emotion['type']})                                                        
        session.commit()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.no)).one()

    @classmethod
    def find_all(cls):
        # return session.query(cls).all()
        return session.query(cls).filter(cls.keyword.like(f'%{keyword}%')).all()

    @staticmethod
    def find_keyword(keyword):
        print('==============find_update==============')
        emotion = session.query(EmotionDto).filter(EmotionDto.keyword.like(f'%{keyword}%')).all()
        if emotion != []:
            print('============중복 검사===========')
        if emotion == []:
            print('============행복회로 가동===========')
            EmotionDao.bulk()

    @classmethod
    def find_by_keyword(cls, keyword):
        return session.query(cls).filter(cls.keyword.like(f'{keyword}')).all()

    @staticmethod
    def test():
        print(' TEST SUCCESS !!')

class StockNewsDao(StockNewsDto):
    @staticmethod
    def bulk():
        emotion_dfo = EmotionDfo()
        stockNews = session.query(StockNewsDto).filter(StockNewsDto.keyword.like(f'%{keyword}%')).all()
        for k, m in enumerate(keyword):
            if m == key1:
                if stockNews == []:
                    df = emotion_dfo.get_df(key1)
                    session.bulk_insert_mappings(StockNewsDto, df.to_dict(orient="records"))
                    session.commit()
                    session.close()
            if m == key2:
                if stockNews == []:
                    df = emotion_dfo.get_df(key2)
                    session.bulk_insert_mappings(StockNewsDto, df.to_dict(orient="records"))
                    session.commit()
                    session.close()
            if m == key3:
                if stockNews == []:
                    df = emotion_dfo.get_df(key3)
                    session.bulk_insert_mappings(StockNewsDto, df.to_dict(orient="records"))
                    session.commit()
                    session.close()

    @staticmethod
    def save(emotion):
        session.add(emotion)
        session.commit()
    
    @staticmethod
    def count():
        return session.query(func.count(StockNewsDto.no)).one()

    @classmethod
    def find_all(cls):
        # return session.query(cls).all()
        return session.query(cls).filter(cls.keyword.like(f'%{keyword}%')).all()

    @classmethod
    def update(cls, emotion):
        emotion = session.query(cls).filter(cls.keyword == keyword).first()\
                .update({cls.no : emotion['no'],\
                cls.positive:emotion['tag'],\
                cls.pos_count:emotion['weight'],\
                cls.negative:emotion['type']})                                                        
        session.commit()

    @staticmethod
    def find_keyword(keyword):
        print('==============find_update==============')
        stockNews = session.query(StockNewsDto).filter(StockNewsDto.keyword.like(f'%{keyword}%')).all()
        if stockNews != []:
            print('============중복 검사===========')

        if stockNews == []:
            print('============Insert===========')
            StockNewsDao.bulk()

    @classmethod
    def find_by_keyword(cls, keyword):
        return session.query(cls).filter(cls.keyword.like(f'{keyword}')).all()


# if __name__ == '__main__':
#     EmotionDao.bulk()