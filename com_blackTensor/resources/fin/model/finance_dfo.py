import csv
import pandas as pd
import os
from pathlib import Path
from com_blackTensor.ext.db import db, openSeesion, engine
from sqlalchemy import func
from com_blackTensor.util.file_hander import FileHandler
from com_blackTensor.resources.emo.model.emotion_kdd import keyword, key1, key2, key3

class FinanceDfo(object):
    def __init__(self):
        print('-----------FinanceDfo--------------')
        self.fileHandler = FileHandler()



    def fina_pro(self, keyword):
        print('----------FinanceDfo----------')
        # df = pd.read_csv('{}_finance.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
        file = pd.read_csv('./csv/{}_finance.csv'.format(keyword), encoding='utf-8-sig')
        # C:/Users/Admin/VscProject/BlackTensor_Test/
        df = pd.DataFrame(file)
        df = df.rename(columns= {
        'Unnamed: 0':'name', '2015/12' : 'f_2015_12', '2016/12' : 'f_2016_12', '2017/12' : 'f_2017_12',
        '2018/12' : 'f_2018_12', '2019/12' : 'f_2019_12', '2020/12(E)' : 'f_2020_12', 
        '2021/12(E)' : 'f_2021_12', '2022/12(E)' : 'f_2022_12'})
        df.to_csv('./csv/{}_finance.csv'.format(keyword), encoding='utf-8-sig')
        print('-----------------fin_file------------------')
        print(df)
        return df
    # fina_pro(0, keyword)
    for k, m in enumerate(keyword):
        if m == key1:
            fina_pro(0, key1)
        if m == key2:
            fina_pro(0, key2)
        if m == key3:
            fina_pro(0, key3)