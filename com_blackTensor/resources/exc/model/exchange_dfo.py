import requests
import pandas as pd
import codecs
import numpy as np
import re
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter
from com_blackTensor.util.file_hander import FileHandler

# # ============================================================
# # ==================                     =====================
# # ==================    Preprocessing    =====================
# # ==================                     =====================
# # ============================================================
# my_folder = '/c/Users/Admin/VscProject/BlackTensor_Test/csv'
class ExchangeDfo(object):
    def __init__(self):
        print('-----------ExchangeDfo--------------')
        self.fileHandler = FileHandler()

    def get_ex_df(self):
    
        df = pd.read_csv('./csv/exchange_index.csv', encoding='utf-8-sig')
        
        df.rename( columns={'Unnamed: 0':'date', '미국 USD':'usd', '일본 JPY':'jpy',\
        '유럽연합 EUR' : 'eur', '중국 CNY' : 'cny'}, inplace=True )
        df = df.sort_values(by=['date'], ascending=True)
        df.drop(df.head(2893).index, inplace=True)
        df = df.reset_index(drop=True)
        df.to_csv('./csv/exchange_reindex.csv', encoding='utf-8-sig')
        print('-----------------Ex_get_df------------------')
        print(df)
        print(type(df))
        return df
    get_ex_df(0)

