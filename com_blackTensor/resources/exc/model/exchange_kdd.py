import pandas as pd
from pandas import DataFrame, Series
import requests as re
from bs4 import BeautifulSoup
import datetime as date
import time

my_folder = '/c/Users/Admin/VscProject/BlackTensor_Test/'

class ExchangeKdd(object):
    def market_index_kdd(self):
        Data = DataFrame()

        url_dict = {'미국 USD':'http://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW',
                    '일본 JPY':'http://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_JPYKRW',
                    '유럽연합 EUR':'http://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_EURKRW',
                    '중국 CNY':'http://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_CNYKRW'}
        for key in url_dict.keys():
            
            date = []
            value = []

            for i in range(1,1000):
                url = re.get(url_dict[key] + '&page=%s'%i)
                url = url.content

                html = BeautifulSoup(url,'html.parser')

                tbody = html.find('tbody')
                tr = tbody.find_all('tr')
                
                
                '''마지막 페이지 까지 받기'''
                if len(tbody.text.strip()) > 3:
                    
                    for r in tr:
                        temp_date = r.find('td',{'class':'date'}).text.replace('.','-').strip()
                        temp_value = r.find('td',{'class':'num'}).text.strip()
                
                        date.append(temp_date)
                        value.append(temp_value)
                else:

                    temp = DataFrame(value, index = date, columns = [key])
                    
                    Data = pd.merge(Data, temp, how='outer', left_index=True, right_index=True)
                    
                    print(key + '자료 수집 완료')
                    time.sleep(10)
                    break
        Data.to_csv('./csv/exchange_index.csv', encoding='utf-8-sig')
        print('==================== 환율 ok ============================')
        print(Data)
        return Data
        '''
                  미국 USD    일본 JPY  유럽연합 EUR  중국 CNY
        2020-11-26  1,106.20  1,060.65  1,319.25  168.65
        2020-11-25  1,107.00  1,060.29  1,317.05  168.54
        2020-11-24  1,110.00  1,064.29  1,318.90  168.76
        2020-11-23  1,112.00  1,072.27  1,321.72  169.40
        2020-11-20  1,117.00  1,075.85  1,324.76  170.11
        ...              ...       ...       ...     ...
        2004-04-19  1,153.60  1,069.63  1,391.47  139.38
        2004-04-16  1,160.10  1,070.20  1,392.00  140.16
        2004-04-14  1,151.30  1,072.87  1,375.23  139.10
        2004-04-13  1,141.10  1,082.12  1,370.23  137.86
        2004-04-12  1,141.80  1,074.13  1,378.38  137.95
        '''
    K = market_index_kdd(0)