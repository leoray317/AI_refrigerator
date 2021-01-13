import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from xgboost import XGBClassifier #model--XGB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier #model --knn
from sklearn.svm import SVC #model-svm
from sklearn.linear_model import LogisticRegression #model--lr
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

mae_list=[]

for name in tqdm.tqdm(name_list):
    xgb_scroe=[]
    rfc_scroe=[]
    svm_scroe=[]
    lr_scroe=[]
    knn_scroe=[]
    lstm_score=[]

    food=[]
    for i in df.values:
        if i[1] == name:
            food.append(i)
    food = pd.DataFrame(food)

    #取得XY
    lsat = food.iloc[:,12].values
    food_X =food.iloc[:,7:].values
    food_y = food.iloc[:,2].values
    food_y = np.array(food_y)
    #food_y = np.array(food_y,dtype = int)

    #標準化
    sc = StandardScaler()
    food_X  = sc.fit_transform(food_X)

    #分割train、test


    #計算共變異數矩陣
    cov_mat = np.cov(food_X.T)
    #計算特徵值與特徵向量
    eigen_vals,eigen_vecs = np.linalg.eig(cov_mat)
    #print('\nEigenvalues \n%s' % eigen_vals)

    tot =sum(eigen_vals)
    var_exp = [(i / tot) for i in sorted(eigen_vals,reverse=True)]
    cum_var_exp = np.cumsum(var_exp)
    #print(var_exp)
    #print(cum_var_exp)

    #plt.bar(range(1,61),var_exp,alpha=0.5,align='center',label='ind exp var')
    #plt.step(range(1,61),cum_var_exp,where='mid',label='cum exp var')
    #plt.ylabel('exp var ratio')
    #plt.xlabel('PC index')
    #plt.legend(loc='best')
    #plt.show()

    X_train, X_test, y_train, y_test = train_test_split(food_X, food_y, test_size=0.3,shuffle=False)
    pca = PCA(n_components = 9)
    X_train = pca.fit_transform(X_train)
    X_test = pca.transform(X_test)
    
    # 建立及訓練模型
    xgb = XGBClassifier()
    rfc = RandomForestClassifier()
    svm = SVC(kernel = 'linear',probability = True)
    lr = LogisticRegression(max_iter=1000)
    knn= KNeighborsClassifier()

    xgb.fit(X_train,y_train)
    xgb_testPredict = xgb.predict(X_test)
    xgb_mae =mean_absolute_error(y_test,xgb_testPredict)

    food_y = np.array(food_y,dtype= int)
    X_train, X_test, y_train, y_test = train_test_split(food_X_pca, food_y, test_size=0.3,shuffle = False)

    rfc.fit(X_train,y_train)
    svm.fit(X_train,y_train)
    lr.fit(X_train,y_train)
    knn.fit(X_train,y_train)

    rfc_testPredict = rfc.predict(X_test)
    svm_testPredict = svm.predict(X_test)
    lr_testPredict = lr.predict(X_test)
    knn_testPredict = knn.predict(X_test)

    rfc_mae =mean_absolute_error(y_test,rfc_testPredict)
    svm_mae =mean_absolute_error(y_test,svm_testPredict)
    lr_mae =mean_absolute_error(y_test,lr_testPredict)
    knn_mae =mean_absolute_error(y_test,knn_testPredict)
    

    
    #LSTM
    sc = StandardScaler()
    food_X  = sc.fit_transform(food_X)

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

    # calculate 均方根誤差(root mean squared error)
    lstm_mae =mean_absolute_error(y_test,testPredict)
    
    last_mae = mean_absolute_error(last, y)

    mae_list.append([name,last_mae,xgb_mae,rfc_mae,svm_mae,lr_mae,knn_mae,lstm_mae])


mse_list_df  = pd.DataFrame(mae_list, columns=['品名','XGB','RFC','SVM','LR','KNN','LSTM'])

mse_list_df.to_csv('4.mae_list.csv_unshuffle.csv',index=False,encoding= 'utf-8-sig')