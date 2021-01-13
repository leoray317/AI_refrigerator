
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
df = pd.read_csv('final1_day.csv')

# 產生 (X, Y) 資料集, Y 是下一期的乘客數
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return np.array(dataX), np.array(dataY)


l = ['青江白菜','蘆筍','奇異果','西瓜','草菇','溼香菇','火龍果','甘藍','熟筍','香蕉']


food_list = []
for i in l:
    food =[]
    for j in df.values:
        if j[3] == i :
            food.append([j[1],j[3],j[5],j[6],j[7],j[11],j[12],j[13],j[14],j[15]])
    df_food = pd.DataFrame(food,columns=['日期','品名','地區','均價','均量','氣溫(℃)','最低氣溫(℃)','相對溼度(%)','風速(m/s)','降水量(mm)'])
    df_food = df_food.sort_values('日期') 
    for f in df_food.values:
        food_list.append(f)

df_food = pd.DataFrame(food_list,columns=['日期','品名','地區','均價','均量','氣溫(℃)','最低氣溫(℃)','相對溼度(%)','風速(m/s)','降水量(mm)'])


food=[]
for j in df_food.values:
    if j[1] == '香蕉':
        food.append([j[3],j[4],j[5],j[6],j[7],j[8],j[9]])
df_num = pd.DataFrame(food,columns=['價','量','氣溫(℃)','最低氣溫(℃)','相對溼度(%)','風速(m/s)','降水量(mm)'])


vol = df_num['量'].tolist()
vol.insert(0,vol[0])
del vol[-1]
df_num['量'] = vol
price = df_num['價'].tolist()
price.insert(0,price[0])
del price[-1]
df_num['過去價格'] = price
#df_num = df_num.drop_duplicates('日期')


#temp =df_num.iloc[:,3]
#info =[]
#for i in df_num.values:
#    info.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
#
#df_info = pd.DataFrame(i) 
#wind = pd.DataFrame(wind,columns =['日期'])



dataset = df_num.values
dataset = dataset.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

x=[]
y=[]
for i in dataset:
    y.append(i[0])
    x.append(i[1:])
    


'''
train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]



look_back = 1

trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
'''

trainX, testX, trainY, testY = train_test_split(np.array(x), np.array(y), test_size=0.33,shuffle = False)


# reshape input to be [samples, time steps, features]
trainX_dim3 = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX_dim3 = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))



# 建立及訓練 LSTM 模型
look_back=7
model = Sequential()
model.add(LSTM(100, input_shape=(10, look_back),return_sequences=True))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(loss='mean_absolute_error', optimizer='adam')
model.fit(trainX_dim3, trainY,epochs=10, batch_size=6, verbose=2,validation_split =0.2)

# 預測
trainPredict = model.predict(trainX_dim3)
testPredict = model.predict(testX_dim3)

#取得真實值
data=[]
for i in dataset[:,0]:
    data.append([i])
data = np.array(data)

#降為二維(MAPE用)
def dim_three_to_two(a):
    l=[]
    for i in a:
        for j in i:
            l.append(j)
    return l
#降為一維(作圖用)    
def dim_two_to_one(a):
    l=[]
    for i in a:
        l.append(i[0])
    return l

trainPre = dim_three_to_two(trainPredict)

testPre = dim_three_to_two(testPredict)

#回復預測資料值為原始數據的規模
#trainPredict = scaler.inverse_transform(trainPre)
#trainY = scaler.inverse_transform(trainY)
#testPredict = scaler.inverse_transform(testPre)
#testY = scaler.inverse_transform(testY)

#mape處理
def mape(y_true, y_pred):
    l=[]
    for i in y_pred:
        l.append(i[0][0])
    mape=[]
    for j in range(len(y_true)):
        a = np.mean(np.abs((y_true[j] - l[j]) / y_true[j])) * 100
        if a < 1000:
            mape.append(a)
    return sum(mape)/len(mape)

#計算MAPE
trainScore = mape(trainY, trainPredict)
print('Train Score: %.2f MAPE' % (trainScore))
testScore = mape(testY, testPredict)
print('Test Score: %.2f MAPE' % (testScore))


#畫train部分
trainPredictPlot = np.empty_like(dim_two_to_one(data))
trainPredictPlot[:] = np.nan
trainPredictPlot[0:len(trainPre)] = trainPre


#畫test部分
testPredictPlot = np.empty_like(dim_two_to_one(data))
testPredictPlot[:] = np.nan
testPredictPlot[len(trainPredict):] = testPre


# 畫原始資料趨勢圖
plt.plot(dim_two_to_one(data))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()
