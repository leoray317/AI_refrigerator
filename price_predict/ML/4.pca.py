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
    food_X =food.iloc[:,7:].values
    food_y = food.iloc[:,2].values
    food_y = np.array(food_y,dtype = int)
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

    pca = PCA(n_components = 9)
    food_X_pca = pca.fit_transform(food_X)
    #print(food_X.shape)
    #print(food_X_pca.shape)

    X_train, X_test, y_train, y_test = train_test_split(food_X_pca, food_y, test_size=0.3)

    # 建立及訓練模型
    xgb = XGBClassifier()
    rfc = RandomForestClassifier()
    svm = SVC(kernel = 'linear',probability = True)
    lr = LogisticRegression(max_iter=1000)
    knn= KNeighborsClassifier()

    scores_xgb = cross_val_score(xgb,food_X_pca,food_y,cv=5,scoring='neg_mean_absolute_error')
    print(scores_xgb.mean())
    scores_rfc = cross_val_score(rfc,food_X_pca,food_y,cv=5,scoring='neg_mean_absolute_error')
    print(scores_rfc.mean())
    scores_svm = cross_val_score(svm,food_X_pca,food_y,cv=5,scoring='neg_mean_absolute_error')
    print(scores_svm.mean())
    scores_lr = cross_val_score(lr,food_X_pca,food_y,cv=5,scoring='neg_mean_absolute_error')
    print(scores_lr.mean())
    scores_knn = cross_val_score(knn,food_X_pca,food_y,cv=5,scoring='neg_mean_absolute_error')
    print(scores_knn.mean())

    
    #LSTM
    sc = StandardScaler()
    food_X  = sc.fit_transform(food_X)

    X_train, X_test, y_train, y_test = train_test_split(food_X, food_y, test_size=0.3)
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
    mae =mean_absolute_error(y_test,testPredict)
    

    mae_list.append([name,scores_xgb.mean(),scores_rfc.mean(),scores_svm.mean(),scores_lr.mean(),scores_knn.mean(),mae])


mse_list_df  = pd.DataFrame(mae_list, columns=['品名','XGB','KNN','SVM','RFC','LR','LSTM'])

mse_list_df.to_csv('4.mae_list.csv',index=False,encoding= 'utf-8-sig')
