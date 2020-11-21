import csv
import json
import pandas as pd
from com_blackTensor.ext.db import db, openSeesion, engine

class UserDto(db.Model):
    
    __tablename__ = 'users'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    email: str = db.Column(db.String(100), primary_key = True, index = True)
    name: str = db.Column(db.String(100))
    password: str = db.Column(db.String(10))
    type: str = db.Column(db.String(10))
    gender: str = db.Column(db.String(10))
    age: int = db.Column(db.Integer)


    def __init__(self, email, name, password, type, gender, age):
        self.email = email
        self.name = name
        self.password = password
        self.type = type
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"User(email={self.email}, name={self.name}, password={self.password}, \
        type={self.type}, gender={self.gender}, age={self.age})"

    
    def __str__(self):
        return f"User(email={self.email}, name={self.name}, password={self.password}, \
        type={self.type}, gender={self.gender}, age={self.age})"

    @property
    def json(self):
        return {
            "email" : self.email,
            "name" : self.name,
            "password" : self.password,
            "type" : self.type,
            "gender" : self.gender,
            "age" : self.age
        }
   

class ReviewDto(db.Model):
    __tablename__ = 'review'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    name: str = db.Column(db.String(100), primary_key = True, index = True)
    money: int = db.Column(db.Integer)
    type: str = db.Column(db.String(10))
    date: str = db.Column(db.String(100))
    price: int = db.Column(db.Integer)
    cnt: int = db.Column(db.Integer)

    # def __init__(self, name, money, type, date, price, cnt):
    #     self.name = name
    #     self.money = money
    #     self.type = type
    #     self.date = date
    #     self.price = price
    #     self.cnt = cnt

    def __repr__(self):
        return f"Review(name={self.name}, money={self.money}, type={self.type}, \
        date={self.date}, price={self.price}, cnt={self.cnt})"

    
    def __str__(self):
        return f"Review(name={self.name}, money={self.money}, type={self.type}, \
        date={self.date}, price={self.price}, cnt={self.cnt})"

    @property
    def json(self):
        return {
            "name" : self.name,
            "money" : self.money,
            "type" : self.type,
            "date" : self.date,
            "price" : self.price,
            "cnt" : self.cnt
        }

class ReviewVo:
    name: str =  ""
    money: int = 0
    type: str = ""
    date: str = ""
    price: int = 0
    cnt: int = 0
    
class UserVo:
    email: str = ""
    name: str = ""
    password: str = ""
    type: str = ""
    gender: str = ""
    age: int = 0