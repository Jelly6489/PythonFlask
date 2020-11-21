from com_blackTensor.resources.covid.status.model.status_dto import CovidStatusDto
from com_blackTensor.ext.db import db, openSeesion

from sqlalchemy import func
# ============================================================
# ==================                     =====================
# ==================       Modeling      =====================
# ==================                     =====================
# ============================================================


# JPA Repository
class CovidStatusDao(CovidStatusDto):
    
    @staticmethod
    def save_data_bulk(datas):
        Session = openSeesion()
        session = Session()

        session.bulk_insert_mappings(CovidStatusDto, datas.to_dict(orient='records'))

        session.commit()
        session.close()
    
    @staticmethod
    def count():
        Session = openSeesion()
        session = Session()
        
        result = session.query(func.count(CovidStatusDto.no)).one()[0]
        session.close()
        return result
    
    @classmethod
    def find_all(self):
        
        Session = openSeesion()
        session = Session()

        result = session.query(CovidStatusDto).all()
        session.close()

        return result
