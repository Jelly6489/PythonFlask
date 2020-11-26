import csv
import pandas as pd
import numpy as np
from com_blackTensor.ext.db import db, openSeesion, engine
from sqlalchemy import func
from com_blackTensor.util.file_hander import FileHandler
from com_blackTensor.resources.emo.model.emotion_kdd import keyword, key1, key2, key3

class StockDfo(object):
    def __init__(self):
        self.fileHandler = FileHandler()  

    def get_df(self, keyword):
        df = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
        # df.drop(df.head(12).index, inplace=True)
        df = df.reset_index(drop=True)

        df.to_csv('./csv/{}_data.csv'.format(keyword), encoding='utf-8-sig')
        print('-----------------get_df------------------')
        print(df)
        print(type(df))
        return df
    # get_df(0, keyword)
    '''
                date      close       open  ...        low      volume  keyword
    0     2015-11-10  1321000.0  1336000.0  ...  1314000.0    197551.0     삼성전자
    1     2015-11-11  1333000.0  1321000.0  ...  1321000.0    140449.0     삼성전자
    2     2015-11-12  1317000.0  1333000.0  ...  1317000.0    157417.0     삼성전자
    3     2015-11-13  1300000.0  1317000.0  ...  1300000.0    177677.0     삼성전자
    4     2015-11-16  1263000.0  1291000.0  ...  1263000.0    275705.0     삼성전자
    ...          ...        ...        ...  ...        ...         ...      ...
    1235  2020-11-20    64700.0    63900.0  ...    63900.0  15068682.0     삼성전자
    1236  2020-11-23    67500.0    64800.0  ...    64700.0  27134398.0     삼성전자
    1237  2020-11-24    67700.0    67900.0  ...    67000.0  32158235.0     삼성전자
    1238  2020-11-25    66600.0    67900.0  ...    66500.0  32447065.0     삼성전자
    1239  2020-11-26    67400.0    66100.0  ...    66000.0  11183078.0     삼성전자
    '''

    for k, m in enumerate(keyword):
        if m == key1:
            get_df(0, key1)
        if m == key2:
            get_df(0, key2)
        if m == key3:
            get_df(0, key3)
    
