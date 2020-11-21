import csv
import json
import pandas as pd
from com_blackTensor.ext.db import db, openSeesion, engine

class EmotionDto(db.Model):
    __tablename__ = 'emotion'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}
    no : int = db.Column(db.Integer, primary_key = True, index = True)
    tag : str = db.Column(db.String(10))
    weight : int = db.Column(db.Integer)
    type : str = db.Column(db.String(10))
    keyword : str = db.Column(db.String(10))
      
    def __repr__(self):
        return f'Emotion(no={self.no}, tag={self.tag}, weight={self.weight}, \
            type={self.type}, keyword={self.keyword})'

    def __str__(self):
        return f'Emotion(no={self.no}, tag={self.tag}, weight={self.weight}, \
            type={self.type}, keyword={self.keyword})'
            
    @property
    def json(self):
        return {
        "no" : self.no,
        "tag" : self.tag,
        "weight" : self.weight,
        "type" : self.type,
        "keyword" : self.keyword
    }

class StockNewsDto(db.Model):
    __tablename__ = 'stock_news'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}
    no : int = db.Column(db.Integer, primary_key = True, index = True)
    title : str = db.Column(db.String(100))
    keyword : str = db.Column(db.String(10))
    
    def __repr__(self):
        return f"Emotion(no={self.no}, title={self.title}, keyword={self.keyword})"

    def __str__(self):
        return f"Emotion(no={self.no}, title={self.title}, keyword={self.keyword})"

    @property
    def json(self):
        return {
        "no" : self.no,
        "title" : self.title,
        "keyword" : self.keyword
    }

class EmotionVo:
    no : int = 0
    tag : str = ""
    weight : int = 0
    type : str = ""
    keyword : str = ""

class StockNewsVo:
    no : int = 0
    title : str = ""
    keyword : str = ""