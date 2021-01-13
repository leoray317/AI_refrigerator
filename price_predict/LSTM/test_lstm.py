
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
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
XGB_MAPE_test=[]
XGB_MAPE_train=[]
for j in df_food.values:
    if j[1] == '甘藍':
        food.append([j[0],j[3],j[4],j[5],j[6],j[7],j[8],j[9]])
df_num = pd.DataFrame(food,columns=['日期','價','量','氣溫(℃)','最低氣溫(℃)','相對溼度(%)','風速(m/s)','降水量(mm)'])
vol = df_num['量'].tolist()
vol.insert(0,vol[0])
del vol[-1]
df_num['量'] = vol
price = df_num['價'].tolist()
price.insert(0,price[0])
del price[-1]
df_num['過去價格'] = price


#temp =df_num.iloc[:,3]
wind =[]
for i in df_num.values:
    wind.append(i[3])
wind = pd.DataFrame(wind,columns =['日期'])


dataset = wind.values
dataset = dataset.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]


look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)

# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))





testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# 建立及訓練 LSTM 模型
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_absolute_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=10, verbose=2,validation_split =0.2)

# 預測
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

print(trainPredict)
'''
# 回復預測資料值為原始數據的規模
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])

# calculate 均方根誤差(root mean squared error)
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

print(dataset)

# 畫訓練資料趨勢圖
# shift train predictions for plotting
trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

# 畫測試資料趨勢圖
# shift test predictions for plotting
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

# 畫原始資料趨勢圖
# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()
'''
