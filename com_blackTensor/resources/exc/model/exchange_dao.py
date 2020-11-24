import csv
import pandas as pd
from com_blackTensor.ext.db import db, openSeesion, engine
from sqlalchemy import func

from com_blackTensor.resources.exc.model.exchange_kdd import ExchangeKdd
from com_blackTensor.resources.exc.model.exchange_dfo import ExchangeDfo
from com_blackTensor.resources.exc.model.exchange_dto import ExchangeDto


Session = openSeesion()
session = Session()

class ExchangeDao(ExchangeDto):
    @staticmethod
    def bulk():
        print('============= Test1 ================')
        exchange_dfo = ExchangeDfo()
        # dfo = stock_dfo.get_df(keyword)
        dfo = exchange_dfo.get_ex_df()
        print('============= Test2 ================')
        session.bulk_insert_mappings(ExchangeDto, dfo.to_dict(orient='records'))
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
        return session.query(cls).all()

    @staticmethod
    def find_by_keyword(keyword):
        return session.query(ExchangeDto).filter(ExchangeDto.keyword.like(f'{keyword}')).all()

