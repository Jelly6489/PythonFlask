import csv
import pandas as pd
from com_blackTensor.ext.db import db, openSeesion, engine
from sqlalchemy import func

from com_blackTensor.resources.sto.model.stock_kdd import StockKdd
from com_blackTensor.resources.sto.model.stock_dto import StockDto
from com_blackTensor.resources.sto.model.stock_dfo import StockDfo
from com_blackTensor.resources.emo.model.emotion_kdd import keyword, key1, key2, key3

Session = openSeesion()
session = Session()

class StockDao(StockDto):
    @staticmethod
    def bulk():
        stock_dfo = StockDfo()
        stock = session.query(StockDto).filter(StockDto.keyword.like(f'%{keyword}%')).all()
        for k, m in enumerate(keyword):
            if m == key1:
                if stock == []:
                    dfo = stock_dfo.get_df(key1)
                    session.bulk_insert_mappings(StockDto, dfo.to_dict(orient='records'))
                    session.commit()
                    session.close()
            if m == key2:
                if stock == []:
                    dfo = stock_dfo.get_df(key2)
                    session.bulk_insert_mappings(StockDto, dfo.to_dict(orient='records'))
                    session.commit()
                    session.close()
            if m == key3:
                if stock == []:
                    dfo = stock_dfo.get_df(key3)
                    session.bulk_insert_mappings(StockDto, dfo.to_dict(orient='records'))
                    session.commit()
                    session.close()

    @staticmethod
    def save(emotion):
        session.add(emotion)
        session.commit()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.date)).one()

    @classmethod
    def find_all(cls):
        # return session.query(cls).all()
        return session.query(cls).filter(cls.keyword.like(f'%{keyword}%')).all()

    @staticmethod
    def test():
        print(' TEST SUCCESS !!')

    @staticmethod
    def find_keyword(keyword):
        print('==============find_update==============')
        stock = session.query(StockDto).filter(StockDto.keyword.like(f'%{keyword}%')).all()
        if stock != []:
            print('============중복 검사===========')
        if stock == []:
            print('============행복회로 가동===========')
            StockDao.bulk()

    @classmethod
    def find_by_keyword(cls, keyword):
        return session.query(cls).filter(cls.keyword.like(f'{keyword}')).all()