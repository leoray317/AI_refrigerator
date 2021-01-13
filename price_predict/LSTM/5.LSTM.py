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
from sklearn.metrics import mean_squared_error
import tqdm

df = pd.read_csv('3.final.csv')

name_list =['青江白菜','蘆筍','奇異果','西瓜','草菇','溼香菇','火龍果','甘藍','熟筍','香蕉']

food=[]
for i in df.values:
    if i[1] == '青江白菜':
        food.append(i)
food = pd.DataFrame(food)

#取得XY
food_X =food.iloc[:,7:].values
food_y = food.iloc[:,2].values
food_y = np.array(food_y,dtype = int)
#food_y = np.array(food_y,dtype = int)

#標準化
sc = StandardScaler()
food_X  = sc.fit_transform(food_X)

#LSTM
X_train, X_test, y_train, y_test = train_test_split(food_X, food_y, test_size=0.3,shuffle = False)
pca = PCA(n_components = 55)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
# reshape input to be [samples, time steps, features]
X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

# 建立及訓練 LSTM 模型
model = Sequential()
model.add(LSTM(55, input_shape=(1, 55)))
model.add(Dense(1))
model.compile(loss='mean_absolute_error', optimizer='adam')
model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=2,validation_split =0.2)

# 預測
trainPredict = model.predict(X_train)
testPredict = model.predict(X_test)


# 畫訓練資料趨勢圖
# shift train predictions for plotting
trainpredict=[]
for i in trainPredict:
    for j in i:
        trainpredict.append(j)
trainPredictPlot = np.empty_like(food_y)
trainPredictPlot[:] = np.nan
trainPredictPlot[0:len(trainpredict)] = trainpredict

# 畫測試資料趨勢圖
# shift test predictions for plotting
testpredict=[]
for i in testPredict:
    for j in i:
        testpredict.append(j)
testPredictPlot = np.empty_like(food_y)
testPredictPlot[:] = np.nan
print(testPredictPlot)
testPredictPlot[len(trainPredict):] = testpredict

# 畫原始資料趨勢圖
# plot baseline and predictions
plt.plot(food_y)
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()
