import numpy as np
from xgboost import XGBClassifier #model--XGB
from sklearn.neighbors import KNeighborsClassifier #model --knn
from sklearn.svm import SVC #model-svm
from sklearn.linear_model import LogisticRegression #model--lr
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import StandardScaler
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import tqdm

def avg(x):
    return sum(x)/len(x)

df = pd.read_csv('final1.csv')

food_df = pd.read_csv('food.csv',encoding='big5')

food = []
for i  in food_df.values:
    food.append(i[0])


mse_list = []

for name in tqdm.tqdm(food):
    try:
        XGB = []
        KNN = []
        SVM = []
        RFC = []
        LR = []
        names = []

        food_list = []
        for j in df.values:
            if j[2] == name:
                food_list.append([j[4],j[5],j[8],j[10],j[11],j[12]])
        df_num = pd.DataFrame(food_list,columns=['均價','均量','氣溫(℃)','相對溼度(%)','風速(m/s)','降水量(mm)'])
        price = df_num['均價'].tolist()
        price.insert(0,price[0])
        del price[-1]
        df_num['過去價格'] = price
        food_X =df_num.iloc[:,1:].values
        food_y = df_num.iloc[:,0]
        food_y = np.array(food_y,dtype = int)

        XGB_MSE = []
        KNN_MSE = []
        SVM_MSE = []
        RFC_MSE = []
        LR_MSE = []
        for i in range(30):
            X_train, X_test, y_train, y_test = train_test_split(food_X, food_y, test_size=0.3)

            sc = StandardScaler()
            sc.fit(X_train)
            X_train = sc.transform(X_train)
            X_test = sc.transform(X_test)

            #XGB
            XGB_model = XGBClassifier()
            #learningrate =0.01, nestimators=20000)
            XGB_model.fit(X_train, y_train)     
            #bst.save_model('test.model')
            y_result_XGB = XGB_model.predict(X_test)

            mse_xgb = mean_squared_error(y_test,y_result_XGB)
            XGB_MSE.append(mse_xgb)

            #KNN
            KNN_model = KNeighborsClassifier()
            KNN_model.fit(X_train, y_train)     
            y_result_KNN = KNN_model.predict(X_test)

            mse_knn = mean_squared_error(y_test,y_result_KNN)
            KNN_MSE.append(mse_knn)

            #SVM
            svm_model = SVC(kernel = 'linear',probability = True)
            svm_model.fit(X_train, y_train)
            y_result_svm = svm_model.predict(X_test)

            mse_svm =mean_squared_error(y_test,y_result_svm)
            SVM_MSE.append(mse_svm)

            #隨機森林

            RFC_model = RandomForestClassifier()
            RFC_model.fit(X_train, y_train)     
            y_result_RFC = RFC_model.predict(X_test)

            mse_RFC =mean_squared_error(y_test,y_result_RFC)
            RFC_MSE.append(mse_RFC)

            #羅吉斯回歸
            LR_model = LogisticRegression()
            LR_model.fit(X_train, y_train)
            y_result_LR = LR_model.predict(X_test)

            mse_LR =mean_squared_error(y_test,y_result_LR)
            LR_MSE.append(mse_LR)


        mse_list.append([name,avg(XGB_MSE),avg(KNN_MSE),avg(SVM_MSE),avg(RFC_MSE),avg(LR_MSE)])
    except:
        print('pass')
        continue

mse_list_df  = pd.DataFrame(mse_list, columns=['品名','XGB','KNN','SVM','RFC','LR'])


mse_list_df.to_csv('mse_list.csv',index=False,encoding= 'utf-8-sig')

'''
importance = XGB_model.feature_importances_
indices = np.argsort(importance)[::-1]
features = pd.DataFrame(X_train).columns
print(importance)
#for f in range(X_train.shape[1]):
#    print(f + 1, 30, features[f], importance[indices[f]])
'''

#ols
'''
est = sm.OLS(y_test,y_result)
est1 = est.fit() 
print('XGB',name,est1.rsquared)
'''

#learning　scure
'''
train_sizes_R,train_score_R,test_score_R = learning_curve(RandomForestClassifier(),food_X,food_y,train_sizes=[0.1,0.2,0.4,0.6,0.8,0.9],cv=3,scoring = 'neg_mean_squared_error')

train_error_R =  np.mean(train_score_R,axis=1)
test_error_R =  np.mean(test_score_R,axis=1)
train_sizes_X,train_score_X,test_score_X = learning_curve(XGBClassifier(),food_X,food_y,train_sizes=[0.1,0.2,0.4,0.6,0.8,0.9],cv=3,scoring = 'mean_squared_error')
train_error_X =   np.mean(train_score_X,axis=1)
test_error_X =  np.mean(test_score_X,axis=1)
plt.figure()
plt.plot(train_sizes_R,train_error_R,'o-',color = 'r',label = 'training_R')
plt.plot(train_sizes_R,test_error_R,'o-',color = 'g',label = 'testing_R')
plt.plot(train_sizes_X,train_error_X,'o-',color = 'b',label = 'training_X')
plt.plot(train_sizes_X,test_error_X,'o-',color = 'black',label = 'testing_X')
plt.legend(loc='best')
plt.xlabel('traing examples')
plt.ylabel('MSE')
plt.show()
#plt.savefig(str(name)+'.png')
'''





