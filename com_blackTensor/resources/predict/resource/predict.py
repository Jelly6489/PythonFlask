from flask_restful import Resource
from flask import request
from flask import jsonify
from com_blackTensor.resources.predict.model.predict_ai import PredictAi

import datetime
import time

import matplotlib as matpl
import matplotlib.pyplot as plt

from com_blackTensor.util.file_hander import FileHandler
from com_blackTensor.util.checker import Checker

class Predict(Resource):
    
    def __init__(self):
        self.ai = PredictAi()
        
    def get(self, stockName:str):        
        # print(f'stock Name : {stockName}')

        if stockName == "삼성전자":
            pred = self.ai.predict_samsung('./csv/samsung.csv')
            pred = int(round(pred))
            return {'pred' : pred, 'stockName' : stockName}
        elif stockName == "셀트리온":
            pred = self.ai.predict_celltrion('./csv/celltrion.csv')
            pred = int(round(pred))
            print(int(round(pred)))
            return {'pred' : pred, 'stockName' : stockName}
        elif stockName == "하나투어":
            pred = self.ai.predict_hana('./csv/hana.csv')
            pred = int(round(pred))
            return {'pred' : pred, 'stockName' : stockName}
        else:
            return {'message' : f'unknown Stock Name. Stock Name : {stockName}'}
  
class PredictDate(Resource):
    
    def __init__(self):
        self.ai = PredictAi()
        matpl.use('Agg')

    def get(self, stockName:str, date:str):

        now = datetime.datetime.now()
        date_obj = None

        try:
            date_obj = datetime.datetime.strptime(date, '%Y%m%d')
        except:
            return {'message' : f'This date is not valid. date : {date}'}
        
        if date_obj > now:
            return {'message' : f'This date is not valid. date : {date}'}
        else:
            
            date = date_obj.strftime('%Y-%m-%d')
            pred_values = []
            real_values = []
            dates = []
            
            if stockName == "삼성전자":
                pred_values, real_values, dates = self.ai.predict_samsung_date('./csv/samsung.csv', date , 5)
            elif stockName == "셀트리온":
                pred_values, real_values, dates = self.ai.predict_samsung_date('./csv/celltrion.csv', date, 5)
            elif stockName == "하나투어":
                pred_values, real_values, dates = self.ai.predict_samsung_date('./csv/hana.csv', date, 5)                
            else:
                return {'message' : f'unknown Stock Name. Stock Name : {stockName}'}
                
            pred_values.reverse()
            real_values.reverse()
            dates.reverse()
            
            millis = int(round(time.time() * 1000))

            if not Checker.check_folder_path('./plt'):
                FileHandler.crete_folder('./plt')    
            
            if len(pred_values) != 0 and len(real_values) != 0 and len(dates) != 0:
                
                plt.figure(facecolor='white', figsize=(20, 10))
                plt.plot(dates, pred_values)
                plt.plot(dates, real_values)

                plt.xlabel('date')
                plt.ylabel('value')
                
                plt.legend(['Pred value', 'True_value'])
                plt.savefig(f'./plt/fredictDate_{millis}.png', dpi=600)
                # plt.show()
                plt.close()

                return_data = []

                for idx in range(0, len(pred_values)):
                    return_data.append({
                        'real': real_values[idx],
                        'pred': pred_values[idx],
                        'date': dates[idx]
                    })
                
                return {'img': Checker.get_abs_path(f'./plt/fredictDate_{millis}.png'), 'datas': return_data}
            else:
                return {'message' : f'Not Include Date In Stock data. Stock Name : {stockName}, date : {date}'}
        

