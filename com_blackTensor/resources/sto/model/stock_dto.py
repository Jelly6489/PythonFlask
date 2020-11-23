import csv
import json
import pandas as pd
from com_blackTensor.ext.db import db, openSeesion, engine

class StockDto(db.Model):
    __tablename__ = 'stock'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}
    no : int = db.Column(db.Integer, primary_key = True, index = True)
    date : str = db.Column(db.String(10))
    close : int = db.Column(db.Integer)
    open : int = db.Column(db.Integer)
    high : int = db.Column(db.Integer)
    low : int = db.Column(db.Integer)
    volume : int = db.Column(db.Integer)
    keyword : str = db.Column(db.String(10))
    def __repr__(self):
        return f"Stock(no={self.no}, date={self.date}, close={self.close}, open={self.open}, high={self.high}, low={self.low}, volume={self.volume}, keyword={self.keyword})"
    def __str__(self):
        return f"Stock(no={self.no}, date={self.date}, close={self.close}, open={self.open}, high={self.high}, low={self.low}, volume={self.volume}, keyword={self.keyword})"
    @property
    def json(self):
        return {
        "no" : self.no,
        "date" : self.date,
        "close" : self.close,
        "open" : self.open,
        "high" : self.high,
        "low" : self.low,
        "volume" : self.volume,
        "keyword" : self.keyword
    }
class StockVo:
    no : int = 0
    date : str = ""
    close : int = 0
    open : int = 0
    high : int = 0
    low : int = 0
    volume : int = 0
    keyword : str = ""