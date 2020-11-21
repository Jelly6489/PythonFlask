from com_blackTensor.ext.db import db, openSeesion

from com_blackTensor.resources.news.economy.model.economy_dto import EconomyNewsDto, EconomyExtractionWordDto
from sqlalchemy import func

class EconomyExtractionWordDao(EconomyExtractionWordDto):
    
    @staticmethod
    def save_data_bulk(datas):
        Session = openSeesion()
        session = Session()

        session.bulk_insert_mappings(EconomyExtractionWordDto, datas.to_dict(orient='records'))

        session.commit()
        session.close()
    
    @staticmethod
    def count():
        Session = openSeesion()
        session = Session()
        
        result = session.query(func.count(EconomyExtractionWordDto.no)).one()[0]
        session.close()
        return result
    
    @classmethod
    def find_all(self):
        
        Session = openSeesion()
        session = Session()

        result = session.query(EconomyExtractionWordDto).all()
        session.close()

        return result

class EconomyNewsDao(EconomyNewsDto):
    
    @staticmethod
    def save_data_bulk(datas):
        Session = openSeesion()
        session = Session()

        session.bulk_insert_mappings(EconomyNewsDto, datas.to_dict(orient='records'))

        session.commit()
        session.close()
    
    @staticmethod
    def count():
        Session = openSeesion()
        session = Session()
        
        result = session.query(func.count(EconomyNewsDto.no)).one()[0]
        session.close()
        return result
    
    @classmethod
    def find_all(self):
        
        Session = openSeesion()
        session = Session()

        result = session.query(EconomyNewsDto).all()
        session.close()

        return result