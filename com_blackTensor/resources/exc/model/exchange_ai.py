import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Activation
from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau
# from sklearn.preprocessing import MinMaxScaler
from com_blackTensor.resources.emo.model.emotion_kdd import keyword, key1, key2, key3
import datetime

class ExchangeAi(object):
    def create_usd(self, keyword): # 미국
        st_data = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0])
        st_data.drop(['keyword'], axis='columns', inplace=True)
        ex_data = pd.read_csv('./csv/exchange_reindex.csv', index_col=[0])
        ex_data.drop(['date', 'jpy', 'eur', 'cny'], axis='columns', inplace=True)
        df = pd.concat([st_data, ex_data], axis=1)
        
        high_price = df['high'].values
        low_price = df['low'].values
        mid_price = (high_price + low_price) /2

        # 최근 50일 데이터를 다음을 예측
        # 50개를 보고 예측하기 때문에 51개씩 저장
        seq_len = 50
        # seq_len = 50
        sequence_length = seq_len + 1
        result = []
        for index in range(len(mid_price) - sequence_length):
            result.append(mid_price[index: index + sequence_length])
            
        try:
            normalized_data = []
            for window in result:
                normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
                normalized_data.append(normalized_window)
        except:
            print('예외 발생!')

        result = np.array(normalized_data)

        # split train and test data
        row = int(round(result.shape[0] * 0.9))
        train = result[:row, :]
        np.random.shuffle(train)

        x_train = train[:, :-1]
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = train[:, -1]

        x_test = result[row:, :-1]
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        y_test = result[row:, -1]

        x_train.shape, x_test.shape
        model = Sequential()

        model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
        model.add(LSTM(62, return_sequences=False))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse', optimizer='rmsprop')
        model.summary()

        model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=10)

        pred = model.predict(x_test)
        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(y_test, label='True')
        ax.plot(pred, label='Prediction')
        plt.title('Stock & USD LSTM')
        ax.legend()
        fig = plt.gcf()
        fig.savefig('./ai_data/{}_LSTM_USD.png'.format(keyword), dpi=fig.dpi)
        # plt.show()
        # =============== 파일 업로드 ===============
        # url = 'http://192.168.0.10:8080/api/stock/lstm_usd'
        # files = {'file': open('./ai_data/{}_LSTM_USD.png'.format(keyword), 'rb')}
        # r = requests.post(url, files=files)
        # ==========================================
    # create_usd(0)
    for k, m in enumerate(keyword):
        if m == key1:
            create_usd(0, key1)
        if m == key2:
            create_usd(0, key2)
        if m == key3:
            create_usd(0, key3)
    def create_jpy(self, keyword): # 일본
        st_data = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0])
        st_data.drop(['keyword'], axis='columns', inplace=True)
        ex_data = pd.read_csv('./csv/exchange_reindex.csv', index_col=[0])
        ex_data.drop(['date', 'usd', 'eur', 'cny'], axis='columns', inplace=True)
        df = pd.concat([st_data, ex_data], axis=1)
        
        high_price = df['high'].values
        low_price = df['low'].values
        mid_price = (high_price + low_price) /2

        # 최근 50일 데이터를 다음을 예측
        # 50개를 보고 예측하기 때문에 51개씩 저장
        seq_len = 50
        # seq_len = 50
        sequence_length = seq_len + 1
        result = []
        for index in range(len(mid_price) - sequence_length):
            result.append(mid_price[index: index + sequence_length])
            
        try:
            normalized_data = []
            for window in result:
                normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
                normalized_data.append(normalized_window)
        except:
            print('예외 발생!')

        result = np.array(normalized_data)

        # split train and test data
        row = int(round(result.shape[0] * 0.9))
        train = result[:row, :]
        np.random.shuffle(train)

        x_train = train[:, :-1]
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = train[:, -1]

        x_test = result[row:, :-1]
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        y_test = result[row:, -1]

        x_train.shape, x_test.shape
        model = Sequential()

        model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
        # model.add(LSTM(50, return_sequences=True, input_shape=(40, 1)))
        model.add(LSTM(62, return_sequences=False))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse', optimizer='rmsprop')
        model.summary()

        model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=10)

        pred = model.predict(x_test)
        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(y_test, label='True')
        ax.plot(pred, label='Prediction')
        plt.title('Stock & JPY LSTM')
        ax.legend()
        fig = plt.gcf()
        fig.savefig('./ai_data/{}_LSTM_JPY.png'.format(keyword), dpi=fig.dpi)
        # plt.show()
    # create_jpy(0)
    for k, m in enumerate(keyword):
        if m == key1:
            create_jpy(0, key1)
        if m == key2:
            create_jpy(0, key2)
        if m == key3:
            create_jpy(0, key3)
    def create_eur(self, keyword): # 유럽 연합
        st_data = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0])
        st_data.drop(['keyword'], axis='columns', inplace=True)
        ex_data = pd.read_csv('./csv/exchange_reindex.csv', index_col=[0])
        ex_data.drop(['date', 'jpy', 'eur', 'cny'], axis='columns', inplace=True)
        df = pd.concat([st_data, ex_data], axis=1)
        
        high_price = df['high'].values
        low_price = df['low'].values
        mid_price = (high_price + low_price) /2

        # 최근 50일 데이터를 다음을 예측
        # 50개를 보고 예측하기 때문에 51개씩 저장
        # seq_len = 50
        seq_len = 50
        sequence_length = seq_len + 1
        result = []
        for index in range(len(mid_price) - sequence_length):
            result.append(mid_price[index: index + sequence_length])
            
        try:
            normalized_data = []
            for window in result:
                normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
                normalized_data.append(normalized_window)
        except:
            print('예외 발생!')

        result = np.array(normalized_data)

        # split train and test data
        row = int(round(result.shape[0] * 0.9))
        train = result[:row, :]
        np.random.shuffle(train)

        x_train = train[:, :-1]
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = train[:, -1]

        x_test = result[row:, :-1]
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        y_test = result[row:, -1]

        x_train.shape, x_test.shape
        model = Sequential()

        model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
        # model.add(LSTM(50, return_sequences=True, input_shape=(40, 1)))
        model.add(LSTM(62, return_sequences=False))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse', optimizer='rmsprop')
        model.summary()

        model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=10)

        pred = model.predict(x_test)
        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(y_test, label='True')
        ax.plot(pred, label='Prediction')
        plt.title('Stock & USD LSTM')
        ax.legend()
        fig = plt.gcf()
        fig.savefig('./ai_data/{}_LSTM_EUR.png'.format(keyword), dpi=fig.dpi)
        # plt.show()
    # create_eur(0)
    for k, m in enumerate(keyword):
        if m == key1:
            create_eur(0, key1)
        if m == key2:
            create_eur(0, key2)
        if m == key3:
            create_eur(0, key3)
    def create_cny(self, keyword): # 중국
        st_data = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0])
        st_data.drop(['keyword'], axis='columns', inplace=True)
        ex_data = pd.read_csv('./csv/exchange_reindex.csv', index_col=[0])
        ex_data.drop(['date', 'jpy', 'eur', 'cny'], axis='columns', inplace=True)
        df = pd.concat([st_data, ex_data], axis=1)
        
        high_price = df['high'].values
        low_price = df['low'].values
        mid_price = (high_price + low_price) /2

        # 최근 50일 데이터를 다음을 예측
        # 50개를 보고 예측하기 때문에 51개씩 저장
        # seq_len = 50
        seq_len = 50
        sequence_length = seq_len + 1
        result = []
        for index in range(len(mid_price) - sequence_length):
            result.append(mid_price[index: index + sequence_length])
            
        try:
            normalized_data = []
            for window in result:
                normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
                normalized_data.append(normalized_window)
        except:
            print('예외 발생!')

        result = np.array(normalized_data)

        # split train and test data
        row = int(round(result.shape[0] * 0.9))
        train = result[:row, :]
        np.random.shuffle(train)

        x_train = train[:, :-1]
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = train[:, -1]

        x_test = result[row:, :-1]
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        y_test = result[row:, -1]

        x_train.shape, x_test.shape
        model = Sequential()

        model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
        # model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
        model.add(LSTM(62, return_sequences=False))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse', optimizer='rmsprop')
        model.summary()

        model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=10)

        pred = model.predict(x_test)
        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(y_test, label='True')
        ax.plot(pred, label='Prediction')
        plt.title('Stock & USD LSTM')
        ax.legend()
        fig = plt.gcf()
        fig.savefig('./ai_data/{}_LSTM_CNY.png'.format(keyword), dpi=fig.dpi)
        # plt.show()
    # create_cny(0)
    for k, m in enumerate(keyword):
        if m == key1:
            create_cny(0, key1)
        if m == key2:
            create_cny(0, key2)
        if m == key3:
            create_cny(0, key3)
    def create_all(self, keyword): # All
        st_data = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0])
        st_data.drop(['keyword'], axis='columns', inplace=True)
        ex_data = pd.read_csv('./csv/exchange_reindex.csv', index_col=[0])
        ex_data.drop(['date'], axis='columns', inplace=True)
        df = pd.concat([st_data, ex_data], axis=1)
        
        high_price = df['high'].values
        low_price = df['low'].values
        mid_price = (high_price + low_price) /2

        # 최근 50일 데이터를 다음을 예측
        # 50개를 보고 예측하기 때문에 51개씩 저장
        # seq_len = 50
        seq_len = 50
        sequence_length = seq_len + 1
        result = []
        for index in range(len(mid_price) - sequence_length):
            result.append(mid_price[index: index + sequence_length])
            
        try:
            normalized_data = []
            for window in result:
                normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
                normalized_data.append(normalized_window)
        except:
            print('예외 발생!')

        result = np.array(normalized_data)

        # split train and test data
        row = int(round(result.shape[0] * 0.9))
        train = result[:row, :]
        np.random.shuffle(train)

        x_train = train[:, :-1]
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = train[:, -1]

        x_test = result[row:, :-1]
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        y_test = result[row:, -1]

        x_train.shape, x_test.shape
        model = Sequential()

        model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
        # model.add(LSTM(50, return_sequences=True, input_shape=(40, 1)))
        model.add(LSTM(62, return_sequences=False))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse', optimizer='rmsprop')
        model.summary()

        model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=10)

        pred = model.predict(x_test)
        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(y_test, label='True')
        ax.plot(pred, label='Prediction')
        plt.title('Stock & All LSTM')
        ax.legend()
        fig = plt.gcf()
        fig.savefig('./ai_data/{}_LSTM_All.png'.format(keyword), dpi=fig.dpi)
        # plt.show()
    # create_all(0)
    for k, m in enumerate(keyword):
        if m == key1:
            create_all(0, key1)
        if m == key2:
            create_all(0, key2)
        if m == key3:
            create_all(0, key3)
    def create_usd_cny(self, keyword): # 미국, 중국
        st_data = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0])
        st_data.drop(['keyword'], axis='columns', inplace=True)
        ex_data = pd.read_csv('./csv/exchange_reindex.csv', index_col=[0])
        ex_data.drop(['date', 'jpy', 'eur' ], axis='columns', inplace=True)
        df = pd.concat([st_data, ex_data], axis=1)
        
        high_price = df['high'].values
        low_price = df['low'].values
        mid_price = (high_price + low_price) /2

        # 최근 50일 데이터를 다음을 예측
        # 50개를 보고 예측하기 때문에 51개씩 저장
        # seq_len = 50
        seq_len = 50
        sequence_length = seq_len + 1
        result = []
        for index in range(len(mid_price) - sequence_length):
            result.append(mid_price[index: index + sequence_length])
            
        try:
            normalized_data = []
            for window in result:
                normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
                normalized_data.append(normalized_window)
        except:
            print('예외 발생!')

        result = np.array(normalized_data)

        # split train and test data
        row = int(round(result.shape[0] * 0.9))
        train = result[:row, :]
        np.random.shuffle(train)

        x_train = train[:, :-1]
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = train[:, -1]

        x_test = result[row:, :-1]
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        y_test = result[row:, -1]

        x_train.shape, x_test.shape
        model = Sequential()

        model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
        # model.add(LSTM(50, return_sequences=True, input_shape=(40, 1)))
        model.add(LSTM(62, return_sequences=False))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse', optimizer='rmsprop')
        model.summary()

        model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=10)

        pred = model.predict(x_test)
        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(y_test, label='True')
        ax.plot(pred, label='Prediction')
        plt.title('Stock & USD_CNY LSTM')
        ax.legend()
        fig = plt.gcf()
        fig.savefig('./ai_data/{}_LSTM_USD_CNY.png'.format(keyword), dpi=fig.dpi)
        # plt.show()
    # create_usd_cny(0)
    for k, m in enumerate(keyword):
        if m == key1:
            create_usd_cny(0, key1)
        if m == key2:
            create_usd_cny(0, key2)
        if m == key3:
            create_usd_cny(0, key3)
    # ======================================================================================================

    # def create_test(self): # Test
    #     st_data = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0])
    #     st_data.drop(['keyword'], axis='columns', inplace=True)
    #     ex_data = pd.read_csv('./csv/exchange_index.csv', index_col=[0])
    #     ex_data.drop(['date', 'jpy', 'eur' ], axis='columns', inplace=True)
    #     # pd.to_datetime(st_data['date'], format='%Y%m%d')
    #     df = pd.concat([st_data, ex_data], axis=1)
        
        
    #     high_price = df['high'].values
    #     low_price = df['low'].values
    #     mid_price = (high_price + low_price) /2

    #     # 최근 50일 데이터를 다음을 예측
    #     # 50개를 보고 예측하기 때문에 51개씩 저장
    #     # seq_len = 50
    #     seq_len = 30
    #     sequence_length = seq_len + 1
    #     result = []
    #     for index in range(len(mid_price) - sequence_length):
    #         result.append(mid_price[index: index + sequence_length])
            
    #     try:
    #         normalized_data = []
    #         for window in result:
    #             normalized_window = [((float(p) / float(window[1])) - 1) for p in window]
    #             normalized_data.append(normalized_window)
    #     except:
    #         print('예외 발생!')

    #     result = np.array(normalized_data)

    #     # split train and test data
    #     row = int(round(result.shape[0] * 0.9))
    #     train = result[:row, :]
    #     np.random.shuffle(train)

    #     x_train = train[:, :-1]
    #     x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    #     y_train = train[:, -1]

    #     x_test = result[row:, :-1]
    #     x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    #     y_test = result[row:, -1]

    #     x_train.shape, x_test.shape
    #     model = Sequential()

    #     model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
    #     # model.add(LSTM(50, return_sequences=True, input_shape=(40, 1)))
    #     model.add(LSTM(62, return_sequences=False))
    #     model.add(Dense(1, activation='linear'))
    #     model.compile(loss='mse', optimizer='rmsprop')
    #     model.summary()

    #     model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=10)

    #     pred = model.predict(x_test)
    #     fig = plt.figure(facecolor='white', figsize=(20, 10))
    #     ax = fig.add_subplot(111)
    #     ax.plot(y_test, label='True')
    #     ax.plot(pred, label='Prediction')
    #     plt.title('Stock & USD_CNY LSTM')
    #     ax.legend()
    #     fig = plt.gcf()
    #     fig.savefig('./ai_data/{}_LSTM_USD_CNY.png'.format(keyword), dpi=fig.dpi)
    #     # plt.show()
    # create_test(0)

    # ======================================================================================================