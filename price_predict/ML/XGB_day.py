import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import statsmodels.api as sm
import tqdm


df = pd.read_csv('total_not_market.csv',encoding = 'utf-8-sig')


l=[]
for i in df.values:
    l.append([i[3],i[5]])


df_l_1 = pd.DataFrame(l,columns=['品名','地區'])
df_l = df_l_1.drop_duplicates(['品名','地區'])


train_test_regrassion = []
for name in tqdm.tqdm(df_l.values):
    try:
        coco = []
        for i in df.values:
            if i[3] == name[0] and i[5] == name[1] :
                coco.append([i[6],i[7]])
        coco_df = pd.DataFrame(coco,columns=['價格','交易量'])
        #iris_three = iris.drop('品名',axis = 1).drop('日期',axis = 1)
        price = coco_df['價格'].tolist()
        del price[0]
        price.append(14.82)
        coco_df['過去價格'] = price
        #climate = pd.read_excel('final.xlsx',encoding = 'utf-8-sig')
        #climate_four = climate.drop("時間", axis = 1).drop('價格',axis = 1).drop('時間.1',axis = 1).drop('相對溼度(%)',axis = 1)
        #
        #combin = pd.concat([iris_three,climate_four],axis=1)
        coco_X =coco_df.iloc[:,1:].values
        coco_y = coco_df.iloc[:,0]
        #iris_y_pro =iris_three.iloc[:,:1].values
        #iris_y_list=[]
        #for i in iris_y_pro:
        #    iris_y_list.append(i[0])
        coco_y = np.array(coco_y,dtype=int)
        #print(coco_X)
        #print(coco_y)
        X_train, X_test, y_train, y_test = train_test_split(coco_X, coco_y, test_size=0.3)
        # fit model no training data
        model = XGBClassifier()
        model.fit(X_train, y_train)
        y_result = model.predict(X_test)
        #predictions = [round(value) for value in y_result]
        #accuracy = accuracy_score(y_test, predictions)
        #print(accuracy)
        #print("Accuracy: %.2f%%" % (accuracy * 100.0))
        est = sm.OLS(y_test,y_result)
        est1 = est.fit() 
        print(est1.rsquared)
    except:
        print('資料量過少')
        continue

train_test_df = pd.DataFrame(train_test_regrassion,columns=['品名','地區','判定係數'])

train_test_df.to_csv('price_volumn_regrassion.csv',encoding = 'utf-8-sig',index = False)

