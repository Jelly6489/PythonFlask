# import sys
# sys.path.insert(0, '/c/Users/Admin/VscProject/BlackTensor_Test/com_blacktensor/cop/fin/model/')
import csv
import pandas as pd
from com_blackTensor.ext.db import db, openSeesion, engine
from sqlalchemy import func

from com_blackTensor.resources.fin.model.finance_kdd import FinanceKdd
from com_blackTensor.resources.fin.model.finance_dfo import FinanceDfo
from com_blackTensor.resources.fin.model.finance_dto import FinanceDto
from com_blackTensor.resources.emo.model.emotion_kdd import keyword, key1, key2, key3
Session = openSeesion()
session = Session()

class FinanceDao(FinanceDto):

    @staticmethod
    def bulk():
        finance_dfo = FinanceDfo()
        finance = session.query(FinanceDto).filter(FinanceDto.keyword.like(f'%{keyword}%')).all()
        for k, m in enumerate(keyword):
            if m == key1:
                if finance == []:
                    dfo = finance_dfo.fina_pro(key1)
                    session.bulk_insert_mappings(FinanceDto, dfo.to_dict(orient='records'))
                    session.commit()
                    session.close()
            if m == key2:
                if finance == []:
                    dfo = finance_dfo.fina_pro(key2)
                    session.bulk_insert_mappings(FinanceDto, dfo.to_dict(orient='records'))
                    session.commit()
                    session.close()
            if m == key3:
                if finance == []:
                    dfo = finance_dfo.fina_pro(key3)
                    session.bulk_insert_mappings(FinanceDto, dfo.to_dict(orient='records'))
                    session.commit()
                    session.close()
        # dfo = finance_dfo.fina_pro(keyword)
        # session.bulk_insert_mappings(FinanceDto, dfo.to_dict(orient='records'))
        # session.commit()
        # session.close()
    
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
        finance = session.query(FinanceDto).filter(FinanceDto.keyword.like(f'%{keyword}%')).all()
        if finance != []:
            print('============중복 검사===========')
        if finance == []:
            print('============행복회로 가동===========')
            FinanceDao.bulk()

    @classmethod
    def find_by_keyword(cls, keyword):
        return session.query(cls).filter(cls.keyword.like(f'{keyword}')).all()
