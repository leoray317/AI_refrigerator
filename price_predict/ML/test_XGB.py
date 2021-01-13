
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
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

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
#dataset = dataset.astype('float32')
#scaler = MinMaxScaler(feature_range=(0, 1))
#dataset = scaler.fit_transform(dataset)



x=[]
y=[]
for i in dataset:
    y.append(i[0])
    x.append(i[1:])

y = np.array(y,dtype = int)

'''
train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]



look_back = 1

trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
'''

trainX, testX, trainY, testY = train_test_split(np.array(x), np.array(y), test_size=0.33,shuffle = False)




# 建立及訓練 XGB 模型
model = XGBClassifier()
model.fit(trainX, trainY)

# 預測
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

data=[]
for i in dataset:
    data.append(i[0])
print(data)

#回復預測資料值為原始數據的規模
#trainPredict = scaler.inverse_transform(dataset)
#trainY = scaler.inverse_transform(trainY)
#testPredict = scaler.inverse_transform(testPre)
#testY = scaler.inverse_transform(testY)

# calculate 均方根誤差(root mean squared error)
def mape(y_true, y_pred):
    mape_list=[]
    for i in range(len(y_pred)):
        mape_list.append(np.mean(np.abs((y_true[i] - y_pred[i]) / y_true[i])) * 100)
    mape=[]
    for j in mape_list:
        if j < 1000 :
            mape.append(j)
    return sum(mape)/len(mape) 


trainScore = mape(trainY, trainPredict)
print('Train Score: %.2f MAPE' % (trainScore))
testScore = mape(testY, testPredict)
print('Test Score: %.2f MAPE' % (testScore))




# 畫訓練資料趨勢圖
# shift train predictions for plotting

trainPredictPlot = np.empty_like(data)
trainPredictPlot[:] = np.nan
trainPredictPlot[0:len(trainPredict)] = trainPredict


# 畫測試資料趨勢圖
# shift test predictions for plotting
testPredictPlot = np.empty_like(data)
testPredictPlot[:] = np.nan
testPredictPlot[len(trainPredict):len(data)] = testPredict
#
#print(testPredictPlot[len(trainPredict)+(look_back*2)+1:len(data)-1, :])
#print(testPre)

# 畫原始資料趨勢圖
# plot baseline and predictions

plt.plot(data)
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.title('XGBoost')
plt.xlabel('time')
plt.ylabel('price')
plt.legend(labels=['ture', 'train','test'],  loc='best')
plt.show()
