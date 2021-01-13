import numpy as np
from xgboost import XGBClassifier #model--XGB
from sklearn.neighbors import KNeighborsClassifier #model --knn
from sklearn.svm import SVC #model-svm
from sklearn.linear_model import LogisticRegression #model--lr
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import StandardScaler
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import tqdm
from sklearn.model_selection import cross_val_score

def mape(y_true, y_pred):
    a = np.mean(np.abs((y_true - y_pred) / y_true) * 100)
    return a

def avg(x):
    return sum(x)/len(x)

df = pd.read_csv('final1_day.csv')

l = ['青江白菜','蘆筍','奇異果','西瓜','草菇','溼香菇','火龍果','甘藍','熟筍','香蕉']


mape_list = []


for name in tqdm.tqdm(l):   
    XGB = []
    KNN = []
    SVM = []
    RFC = []
    LR = []
    food_list = []
    for j in df.values:
        if j[3] == name:
            food_list.append([j[6],j[7],j[11],j[12],j[13],j[14],j[15]])
    df_num = pd.DataFrame(food_list,columns=['均價','均量','氣溫(℃)','最低氣溫(℃)','相對溼度(%)','風速(m/s)','降水量(mm)'])
    price = df_num['均價'].tolist()
    price.insert(0,price[0])
    del price[-1]
    df_num['過去價格'] = price
    food_X =df_num.iloc[:,1:].values
    food_y = df_num.iloc[:,0]
    food_y = np.array(food_y,dtype = int)

    sc = StandardScaler()
    sc.fit(food_X)
    
    food_X = sc.transform(food_X)
    

    XGB_cv = []
    KNN_cv = []
    SVM_cv = []
    RFC_cv = []
    LR_cv = []
    
    #X_train, X_test, y_train, y_test = train_test_split(food_X, food_y, test_size=0.3,shuffle=False)

    #XGB
    XGB_model = XGBClassifier(min_child_weight=0.1,max_depth=7)
    
    #KNN
    KNN_model = KNeighborsClassifier()

    #SVM
    SVM_model = SVC(kernel = 'linear',probability = True)

    #隨機森
    RFC_model = RandomForestClassifier(n_estimators=100,n_jobs=5)

    #羅吉斯回歸
    LR_model = LogisticRegression()

    scores_x = cross_val_score(XGB_model,food_X,food_y,cv=5,scoring='neg_root_mean_squared_error')
    scores_k = cross_val_score(KNN_model,food_X,food_y,cv=5,scoring='neg_root_mean_squared_error')
    scores_s = cross_val_score(SVM_model,food_X,food_y,cv=5,scoring='neg_root_mean_squared_error')
    scores_r = cross_val_score(RFC_model,food_X,food_y,cv=5,scoring='neg_root_mean_squared_error')
    scores_l = cross_val_score(LR_model,food_X,food_y,cv=5,scoring='neg_root_mean_squared_error')

    sm_x = -scores_x.mean()
    sm_k = -scores_k.mean()
    sm_s = -scores_s.mean()
    sm_r = -scores_r.mean()
    sm_l = -scores_l.mean()



    mape_list.append([name,sm_x,sm_k,sm_s,sm_r,sm_l])



mape_list_df  = pd.DataFrame(mape_list, columns=['品名','XGB','KNN','SVM','RFC','LR'])


mape_list_df.to_csv('mape_list_unshuffle_test.csv',index=False,encoding= 'utf-8-sig')
