import csv
import json
import pandas as pd
from com_blackTensor.ext.db import db, openSeesion, engine

class ExchangeDto(db.Model):
    __tablename__ = 'exchange'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}
    no : int = db.Column(db.Integer, primary_key = True, index = True)
    date : str = db.Column(db.String(10))
    usd : str = db.Column(db.String(10))
    jpy : str = db.Column(db.String(10))
    eur : str = db.Column(db.String(10))
    cny : str = db.Column(db.String(10))

    def __repr__(self):
        return f"Stock(no={self.no}, date={self.date}, usd={self.usd}, jpy={self.jpy}, eur={self.eur}, cny={self.cny})"

    def __str__(self):
        return f"Stock(no={self.no}, date={self.date}, usd={self.usd}, jpy={self.jpy}, eur={self.eur}, cny={self.cny})"

    @property
    def json(self):
        return {
        "no" : self.no,
        "date" : self.date,
        "usd" : self.usd,
        "jpy" : self.jpy,
        "eur" : self.eur,
        "cny" : self.cny
    }

class StockVo:
    no : int = 0
    date : str = ""
    usd : str = ""
    jpy : str = ""
    eur : str = ""
    cny : str = ""
