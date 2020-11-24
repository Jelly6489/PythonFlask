import csv
import pandas as pd
from com_blackTensor.ext.db import db, openSeesion, engine
from sqlalchemy import func
from com_blackTensor.usr.model.user_dfo import UserDfo
from com_blackTensor.usr.model.user_dto import UserDto, ReviewDto

Session = openSeesion()
session = Session()

class UserDao(UserDto):
    
    @staticmethod
    # def bulk(cls, user_dfo):
    def bulk():
        user_dfo = UserDfo()
        dfo = user_dfo.create()
        print(dfo.head())
        session.bulk_insert_mappings(UserDto, dfo.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def save(user):
        session.add(user)
        session.commit()

    # @classmethod
    # def update(cls, user):
    #     session.query(cls).filter(cls.email == user['email'])\
    #         .update({cls.password:user['password'],\
    #             cls.pclass:user['pclass'],\
    #             cls.embarked:user['embarked']})                                                        
    #     session.commit()

    @classmethod
    def delete(cls, email):
        data = cls.query.get(email)
        db.session.delete(data)
        db.session.commit()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.email)).one()

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    
    '''
    SELECT *
    FROM users
    WHERE user_name LIKE 'a'
    '''
    # like() method itself produces the LIKE criteria 
    # for WHERE clause in the SELECT expression.
    
    @classmethod
    def find_one(cls, email):
        return session.query(cls)\
            .filter(cls.email == email).one()

    '''
    SELECT *
    FROM users
    WHERE user_id LIKE '1' AND password LIKE '1'
    '''
    @classmethod
    def login(cls, user):
        print('=======Test login=======')
        return session.query(cls).filter(cls.email == user.email, cls.password == user.password).one()

    # '''
    # SELECT *
    # FROM users
    # WHERE user_name LIKE 'name'
    # '''
    # # the meaning of the symbol %
    # # A% ==> Apple
    # # %A ==> NA
    # # %A% ==> Apple, NA, BAG 
    # @classmethod
    # def find_by_name(cls, name):
    #     return session.query(cls).filter(cls.email.like(f'%{name}%')).all()

    # '''
    # SELECT *
    # FROM users
    # WHERE user_id IN (start, end)
    # '''
    # # List of users from start to end ?
    # @classmethod
    # def find_users_in_category(cls, start, end):
    #     return session.query(cls)\
    #                   .filter(cls.user_id.in_([start,end])).all()

    # '''
    # SELECT *
    # FROM users
    # WHERE gender LIKE 'gender' AND name LIKE 'name%'
    # '''
    # # Please enter this at the top. 
    # # from sqlalchemy import and_
    # @classmethod
    # def find_users_by_gender_and_name(cls, gender, name):
    #     return session.query(cls)\
    #                   .filter(and_(cls.gender.like(gender),
    #                    cls.name.like(f'{name}%'))).all()

    # '''
    # SELECT *
    # FROM users
    # WHERE pclass LIKE '1' OR age_group LIKE '3'
    # '''
    # # Please enter this at the top. 
    # # from sqlalchemy import or_
    # @classmethod
    # def find_users_by_gender_and_name(cls, gender, age_group):
    #     return session.query(cls)\
    #                   .filter(or_(cls.pclass.like(gender),
    #                    cls.age_group.like(f'{age_group}%'))).all()
    


class ReviewDao(ReviewDto):
    
    @staticmethod
    # def bulk(cls, user_dfo):
    def bulk():
        review_dfo = UserDfo()
        dfo = review_dfo.get_mypage()
        print(dfo.head())
        session.bulk_insert_mappings(ReviewDto, dfo.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def save(review):
        session.add(review)
        session.commit()

    # @classmethod
    # def update(cls, user):
    #     session.query(cls).filter(cls.email == user['email'])\
    #         .update({cls.password:user['password'],\
    #             cls.pclass:user['pclass'],\
    #             cls.embarked:user['embarked']})                                                        
    #     session.commit()

    @classmethod
    def delete(cls, username):
        data = cls.query.get(username)
        db.session.delete(data)
        db.session.commit()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.username)).one()

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    
    '''
    SELECT *
    FROM users
    WHERE user_name LIKE 'a'
    '''
    # like() method itself produces the LIKE criteria 
    # for WHERE clause in the SELECT expression.
    
    @classmethod
    def find_one(cls, username):
        return session.query(cls)\
            .filter(cls.username == username).one()

    @classmethod
    def find_by_name(cls, username):
        return session.query(cls).filter(cls.username.like(f'{username}')).one()

