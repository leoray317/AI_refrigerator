import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_absolute_error
import tqdm

def avg(c):
    a=sum(c)/len(c)
    return a

def movavg(num,a):
    p=[]
    for i in range(num):
        p.append(a[i])

    for j in range(len(a)-num):
        t=[]
        for k in  range(num):
            t.append(a[k+j])
        p.append(round(avg(t),2))
    return p



name_list =['奇異果','西瓜','草菇','溼香菇','火龍果','甘藍','熟筍','香蕉']

for name in tqdm.tqdm(name_list):
    df = pd.read_csv('3.final.csv')
    food = []
    new_x = []
    for i in df.values:
        if i[1] == name:
            food.append([i[0],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]])
            new_x.append(i[2])

    df = pd.DataFrame(food,columns =['日期','平均價格','上價','中價','下價','交易量','月前氣溫','月前最低氣溫','月前相對溼度','月前風速','月前降水量'] )

    date = df['日期']
    price = df['平均價格']
    up_price = df['上價']
    mid_price = df['中價']
    low_price = df['下價']
    volumn = df['交易量']
    temp = df['月前氣溫']
    low_temp = df['月前最低氣溫']
    wet = df['月前相對溼度']
    wind = df['月前風速']
    rain = df['月前降水量']


    l=[price,up_price,mid_price,low_price,volumn,temp,low_temp,wet,wind,rain]
    k=['price','up_price','mid_price','low_price','volumn','temp','low_temp','wet','wind','rain']
    for a,i in enumerate(l):
        li=[]
        for j in i:
            li.append(j)

        df = pd.DataFrame(li,columns=['平均價格'])

        df['月前一日移動平均溫'] = movavg(1,i)
        df['月前五日移動平均溫'] = movavg(5,i)
        df['月前十日移動平均溫'] = movavg(10,i)
        df['月前二十日移動平均溫'] = movavg(20,i)
        df['月前五十日移動平均溫'] = movavg(50,i)
        df['月前百日移動平均溫'] = movavg(100,i)

        X =df.iloc[:,1:].values
        y = df.iloc[:,0].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,shuffle=False)
        #reshape input to be [samples, time steps, features]
        X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
        X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

        # 建立及訓練 LSTM 模型
        model = Sequential()
        model.add(LSTM(11, input_shape=(1,6)))
        model.add(Dense(1))
        model.compile(loss='mean_absolute_error', optimizer='adam')
        model.fit(X_train, y_train, epochs=200, batch_size=10, verbose=2,validation_split =0.2)

        # 預測
        trainPredict = model.predict(X_train)
        testPredict = model.predict(X_test)

        model.save(str(name)+'_'+ str(k[a])+ '_model.h5')