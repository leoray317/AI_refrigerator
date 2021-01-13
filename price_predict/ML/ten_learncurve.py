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


df = pd.read_csv('final1_day.csv')

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




for i in l:
    food=[]
    XGB_MAPE_test=[]
    XGB_MAPE_train=[]
    for j in df_food.values:
        if j[1] == i:
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

    
    food_X =df_num.iloc[:,1:].values
    food_y = df_num.iloc[:,0]
    food_y = np.array(food_y,dtype = int)

    '''
    train_sizes_L,train_score_L,test_score_L = learning_curve(XGBClassifier(eta = 0.3,max_depth = 6,gamma = 1.5),food_X,food_y,cv=3,shuffle = False,scoring = 'neg_mean_absolute_error')
    train_error_L =   np.mean(-train_score_L,axis=1)
    test_error_L=  np.mean(-test_score_L,axis=1)

    plt.figure()
    plt.plot(train_sizes_L,train_error_L,'o-',color = 'green',label = 'training_L')
    plt.plot(train_sizes_L,test_error_L,'o-',color = 'yellow',label = 'testing_L')
    plt.legend(loc='best')
    plt.xlabel('traing examples')
    plt.ylabel('MAPE')
    #plt.show()
    plt.savefig(str(i)+'.png')
    '''
    size = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    for size in size:
        X_train, X_test, y_train, y_test = train_test_split(food_X, food_y, train_size= size ,shuffle = False)
        #sc = StandardScaler()
        #sc.fit(X_train)
        #X_train = sc.transform(X_train)
        #X_test = sc.transform(X_test)

        XGB_model = XGBClassifier()
        #learningrate =0.01, nestimators=20000)
        XGB_model.fit(X_train, y_train)     
        #bst.save_model('test.model')
        y_result_XGB = XGB_model.predict(X_test)
        y_test_XGB = XGB_model.predict(X_train)
        mape_xgb_test = np.mean(np.abs((y_test - y_result_XGB) / y_test))
        mape_xgb_train = np.mean(np.abs((y_train - y_test_XGB) / y_train))
        XGB_MAPE_test.append(mape_xgb_test)
        XGB_MAPE_train.append(mape_xgb_train)
        

    plt.figure()
    plt.plot(XGB_MAPE_test,'o-',color = 'red',label = 'testing_L')
    plt.plot(XGB_MAPE_train,'o-',color = 'blue',label = 'training_L')
    plt.legend(loc='best')
    plt.xlabel('traing examples')
    plt.ylabel('MAPE')
    #plt.show()
    plt.savefig(str(i)+'.png')


