from sklearn import datasets   #數據庫
from sklearn.cluster import KMeans #訓練方式
import pandas as pd
import numpy as np
from matplotlib import pyplot  as plt

df = pd.read_csv('total_same_name.csv',encoding='utf-8-sig')
df=df.sort_values(by=['產品碼'])

df = df.drop(df[ df['產品名'] == '休市' ].index)


code=[]
for i in df.values:
    code.append(i[3])

code_list = []
code = pd.DataFrame(code,columns = ['name'])
code = code.drop_duplicates(['name'])
code = code.values
for i in code:
    code_list.append(i[0])

volatility_list=[]
for i in code_list:
    volatility_i =[]
    volatility = []
    for total_list in df.values:
        if total_list[3] == i:
            volatility.append(total_list[7])

    volatility_value = round(100*(np.percentile(volatility,75)-np.percentile(volatility,25))/(sum(volatility)/len(volatility)),2)
    avg_price = round(sum(volatility)/len(volatility),2)
    #print(str(i)+'的波動度:'+str(round(100*volatility_value,3))+'%')
    volatility_i.append(i)
    volatility_i.append(volatility_value)
    volatility_i.append(avg_price)
    volatility_list.append(volatility_i)
    print(volatility_i)


volatility_df = pd.DataFrame(volatility_list,columns=['品名','波動率','平均價格'])
volatility_df.to_csv('volatility.csv',encoding = 'utf-8-sig',index = False)





