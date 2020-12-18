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
        # df.to_csv('./csv/{}_finance.csv'.format(keyword), encoding='utf-8-sig')
        print('-----------------fin_file------------------')
        print(df)
        return df
        '''
                name   f_2015_12   f_2016_12   f_2017_12   f_2018_12   f_2019_12   f_2020_12   f_2021_12   f_2022_12 keyword
        0          매출액  2006535.00  2018667.00  2395754.00  2437714.00  2304009.00  2384040.00  2605090.00  2814636.00    삼성전자
        1         영업이익   264134.00   292407.00   536450.00   588867.00   277685.00   371055.00   461792.00   552196.00    삼성전자
        2   영업이익(발표기준)   264134.00   292407.00   536450.00   588867.00   277685.00        0.00        0.00        0.00   삼성전자
        3        당기순이익   190601.00   227261.00   421867.00   443449.00   217389.00   278835.00   350988.00   420633.00    삼성전자
        4      지배주주순이익   186946.00   224157.00   413446.00   438909.00   215051.00   276410.00   347797.00   416810.00    삼성전자
        5     비지배주주순이익     3655.00     3104.00     8422.00     4540.00     2338.00        0.00        0.00        0.00   삼성전자
        6         자산총계  2421795.00  2621743.00  3017521.00  3393572.00  3525645.00  3754147.00  4046552.00  4408017.00    삼성전자
        7         부채총계   631197.00   692113.00   872607.00   916041.00   896841.00   926779.00   979519.00  1027791.00    삼성전자
        8         자본총계  1790598.00  1929630.00  2144914.00  2477532.00  2628804.00  2827582.00  3067152.00  3380613.00    삼성전자
        9       지배주주지분  1728768.00  1864243.00  2072134.00  2400690.00  2549155.00  2744279.00  2983815.00  3296286.00    삼성전자
        10     비지배주주지분    61830.00    65387.00    72780.00    76842.00    79649.00    83303.00    83337.00    84327.00    삼성전자
        11         자본금     8975.00     8975.00     8975.00     8975.00     8975.00     8979.00     8979.00     8979.00    삼성전자
        12        부채비율       35.25       35.87       40.68       36.97       34.12       32.78       31.94       30.40    삼성전자
        13         유보율    20659.47    21757.56    23681.42    26648.22    28302.40        0.00        0.00        0.00    삼성전자
        14       영업이익률       13.16       14.49       22.39       24.16       12.05       15.56       17.73       19.62    삼성전자
        15    지배주주순이익률        9.32       11.10       17.26       18.00        9.33       11.59       13.35       14.81   삼성전자
        16         ROA        8.07        9.01       14.96       13.83        6.28        7.66        9.00        9.95    삼성전자
        17         ROE       11.16       12.48       21.01       19.63        8.69       10.44       12.14       13.27    삼성전자
        18         EPS     2198.00     2735.00     5421.00     6024.00     3166.00     4069.00     5120.00     6136.00    삼성전자
        19         BPS    21903.00    24340.00    28971.00    35342.00    37528.00    40401.00    43927.00    48527.00    삼성전자
        20         DPS      420.00      570.00      850.00     1416.00     1416.00     1561.00     1560.00     1543.00    삼성전자
        21         PER       11.47       13.18        9.40        6.42       17.63       16.37       13.01       10.85    삼성전자
        22         PBR        1.15        1.48        1.76        1.10        1.49        1.65        1.52        1.37    삼성전자
        23       발행주식수  7364967.00  7033967.00  6454925.00  5969783.00  5969783.00        0.00        0.00        0.00    삼성전자
        24       배당수익률        1.67        1.58        1.67        3.66        2.54        0.00        0.00        0.00    삼성전자
        '''
    # fina_pro(0, keyword)
    for k, m in enumerate(keyword):
        if m == key1:
            result = fina_pro(0, key1)
            df = pd.DataFrame(result)
            df.loc[:, 'keyword'] = key1
            print('--------fin_file-----------')
            print(df.head())
            df.to_csv('./csv/{}_finance.csv'.format(key1), encoding='utf-8-sig')
        if m == key2:
            result = fina_pro(0, key2)
            df = pd.DataFrame(result)
            df.loc[:, 'keyword'] = key2
            print('--------fin_file-----------')
            print(df.head())
            df.to_csv('./csv/{}_finance.csv'.format(key2), encoding='utf-8-sig')
        if m == key3:
            result = fina_pro(0, key3)
            df = pd.DataFrame(result)
            df.loc[:, 'keyword'] = key3
            print('--------fin_file-----------')
            print(df.head())
            df.to_csv('./csv/{}_finance.csv'.format(key3), encoding='utf-8-sig')