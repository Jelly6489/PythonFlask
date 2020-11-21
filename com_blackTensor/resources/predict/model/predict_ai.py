import pandas as pd
import numpy as np
import datetime

from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

from com_blackTensor.util.file_hander import FileHandler
from com_blackTensor.util.checker import Checker
class PredictAi(object):

    def __init__(self):
        # print()
        self.samsung_model = load_model(Checker.get_abs_path('./model/samsung.h5'))
        self.celltrion_model = load_model(Checker.get_abs_path('./model/celltrion.h5'))
        self.hana_model = load_model(Checker.get_abs_path('./model/hana.h5'))
    
    def predict_samsung(self, csv_path):
        datas = FileHandler.load_to_csv(csv_path, 'utf-8 sig')
        return self.predict_data(self.samsung_model, datas)
    
    def predict_celltrion(self, csv_path):
        datas = FileHandler.load_to_csv(csv_path, 'utf-8 sig')
        return self.predict_data(self.celltrion_model, datas)
    
    def predict_hana(self, csv_path):
        datas = FileHandler.load_to_csv(csv_path, 'utf-8 sig')
        return self.predict_data(self.hana_model, datas)
    
    def predict_data(self, model, datas):

        pred_stock = datas[-50:]
        pred_stock = pred_stock['close']

        pred_stock = pred_stock.tolist()
        pred_stock = np.array(pred_stock)
        # print(pred_stock.shape)
        pred_stock = np.reshape(pred_stock, (50, 1))

        scaler = MinMaxScaler()
        pred_stock = scaler.fit_transform(pred_stock)
        # print(type(pred_stock))
        pred_stock = np.array(pred_stock)
        
        pred_stock = np.reshape(pred_stock, (1, 50, 1))

        pred_stock = model.predict(pred_stock)
        
        pred_stock = scaler.inverse_transform(pred_stock)
        pred_stock = np.reshape(pred_stock, 1)

        # print(f'pred_stock : {pred_stock}')

        return pred_stock[0]
        
    def predict_samsung_date(self, csv_path, date, repeat_count):
        data = FileHandler.load_to_csv(csv_path, 'utf-8 sig')       
        pred_values, real_values, dates = self.predict_data_with_time(self.samsung_model, data, date, repeat_count)

        return pred_values, real_values, dates

    def predict_celltrion_date(self, csv_path, date, repeat_count):
        data = FileHandler.load_to_csv(csv_path, 'utf-8 sig')
        pred_values, real_values, dates = self.predict_data_with_time(self.celltrion_model, data, date, repeat_count)

        return pred_values, real_values, dates

    def predict_hana_date(self, csv_path, date, repeat_count):
        data = FileHandler.load_to_csv(csv_path, 'utf-8 sig')
        pred_values, real_values, dates = self.predict_data_with_time(self.hana_model, data, date, repeat_count)

        return pred_values, real_values, dates
    
    def predict_data_with_time(self, model, data, date, repeat_count):
        
        real_values = []
        pred_values = []
        date_values = []

        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        date = date.strftime('%Y-%m-%d')

        # print(f't_date : {date}')

        idx = self.get_data_use_date(data, date)
        # print(f'idx value : {idx}')

        if idx != -1:
            for index in range(0, repeat_count):
                end_index = idx-index
                # print(f'end_index value : {end_index}')

                real_value = -1
                date_keys = ''
                # print(len(data))

                if len(data) == (end_index+1):
                    real_value = int(data[-1:]['close'].values[0])
                    date_keys = data[-1:]['date'].values[0]
                else:
                    real_value = int(data[end_index:(end_index+1)]['close'].values[0])
                    date_keys = data[end_index:(end_index+1)]['date'].values[0]

                # print(f'date_keys : {date_keys}')
                date_values.append(date_keys)
                
                # print(f'real_value : {real_value}')

                real_values.append(real_value)
                # print(f'datas : {data[:end_index]}')
                
                pred_value = self.predict_data(model, data[:end_index])
                pred_values.append(int(pred_value))

            # print(f'pred_values : {pred_values}')
            # print(f'real_values : {real_values}')
            return pred_values, real_values, date_values
        else:
            return [], [], []

        return pred_values.reverse(), real_values.reverse()

    def get_data_use_date(self, data, date):
        idx_list = data.index[data['date'] == date].tolist()
        # print(f'idx_list : {idx_list}')

        if len(idx_list) == 0:
            return -1
        else:
            return idx_list[0]
            