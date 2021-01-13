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

name_list =['青江白菜','蘆筍','奇異果','西瓜','草菇','溼香菇','火龍果','甘藍','熟筍','香蕉']
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

  model = load_model(name+'_price_model.h5')

  price_list=[]
  for i in price:
      price_list.append(i)

  for j in range(30):
      df = pd.DataFrame(price_list,columns=['price'])
      price = df['price']
      df['一'] = movavg(1,price)
      df['五'] = movavg(5,price)
      df['十'] = movavg(10,price)
      df['二十'] = movavg(20,price)
      df['五十'] = movavg(50,price)
      df['百'] = movavg(100,price)

      X =df.iloc[:,1:].values

      x=model.predict(np.reshape(X[-1], (1, 1, X[-1].shape[0])))
      price_list.append(round(x[0,0],1))
  df_new = pd.DataFrame(price_list,columns=['平均價格'])

  l=[up_price,mid_price,low_price,volumn,temp,low_temp,wet,wind,rain]
  k=['up_price','mid_price','low_price','volumn','temp','low_temp','wet','wind','rain']
  zh = ['上價','中價','下價','交易量','月前氣溫','月前最低氣溫','月前相對溼度','月前風速','月前降水量']

  for num,column in enumerate(l): 
    model = load_model(name +'_' + k[num] +'_model.h5')

    li=[]
    for i in column:
        li.append(i)

    for j in range(30):
        df = pd.DataFrame(li,columns=[k[num]])
        price = df[k[num]]
        df['一'] = movavg(1,price)
        df['五'] = movavg(5,price)
        df['十'] = movavg(10,price)
        df['二十'] = movavg(20,price)
        df['五十'] = movavg(50,price)
        df['百'] = movavg(100,price)

        X =df.iloc[:,1:].values

        x=model.predict(np.reshape(X[-1], (1, 1, X[-1].shape[0])))
        li.append(round(x[0,0],1))
    df_new[zh[num]] = li
    print(df_new)
    
  df_new.to_csv(name +'_預測.csv',encoding='utf-8-sig',index=False)
  