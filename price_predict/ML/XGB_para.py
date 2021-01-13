import numpy as np
from xgboost import XGBClassifier #model--XGB
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import learning_curve
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import tqdm


df = pd.read_csv('final1.csv')
df = df.sort_values(by=['時間'])


food_df = pd.read_csv('food.csv',encoding='big5')

food = []
for i  in food_df.values:
    food.append(i[0])





XGB_MSE = []
food_list = []

for j in df.values:
    if j[2] == '香蕉':
        food_list.append([j[4],j[5],j[8],j[10],j[11],j[12]])
df_num = pd.DataFrame(food_list,columns=['均價','均量','氣溫(℃)','相對溼度(%)','風速(m/s)','降水量(mm)'])
vol = df_num['均量'].tolist()
vol.insert(0,vol[0])
del vol[-1]
df_num['均量'] = vol

price = df_num['均價'].tolist()
price.insert(0,price[0])
del price[-1]
df_num['過去價格'] = price




food_X =df_num.iloc[:,1:].values
food_y = df_num.iloc[:,0]
food_y = np.array(food_y,dtype = int)


'''
for i in range(30):
    X_train, X_test, y_train, y_test = train_test_split(food_X, food_y, test_size=0.3)
    sc = StandardScaler()
    sc.fit(X_train)
    X_train = sc.transform(X_train)
    X_test = sc.transform(X_test)
    
    XGB_model = XGBClassifier()
    #learningrate =0.01, nestimators=20000)
    XGB_model.fit(X_train, y_train)     
    #bst.save_model('test.model')
    y_result_XGB = XGB_model.predict(X_test)
    mse_xgb = mean_squared_error(y_test,y_result_XGB)
    XGB_MSE.append(mse_xgb)

'''


train_sizes_T,train_score_T,test_score_T = learning_curve(XGBClassifier(),food_X,food_y,cv= 3,shuffle = False,scoring = 'neg_root_mean_squared_error')
train_error_T =   np.mean(-train_score_T,axis=1)
test_error_T =  np.mean(-test_score_T,axis=1)

train_sizes_L,train_score_L,test_score_L = learning_curve(XGBClassifier(booster = 'gbtree',eta = 0.2,max_depth = 6,gamma = 0),food_X,food_y,cv=3,shuffle = False,scoring = 'neg_root_mean_squared_error')
train_error_L =   np.mean(-train_score_L,axis=1)
test_error_L=  np.mean(-test_score_L,axis=1)

plt.figure()
plt.plot(train_sizes_T,train_error_T,'o-',color = 'red',label = 'training_T')
plt.plot(train_sizes_T,test_error_T,'o-',color = 'black',label = 'testing_T')
plt.plot(train_sizes_L,train_error_L,'o-',color = 'green',label = 'training_L')
plt.plot(train_sizes_L,test_error_L,'o-',color = 'yellow',label = 'testing_L')
plt.legend(loc='best')
plt.xlabel('traing examples')
plt.ylabel('MSE')
plt.show()
#plt.savefig(str(name)+'.png')
