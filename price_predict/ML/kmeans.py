from sklearn import datasets   #數據庫
from sklearn.cluster import KMeans #訓練方式
import pandas as pd
import numpy as np
from matplotlib import pyplot  as plt

df = pd.read_csv('volatility.csv',encoding='utf-8-sig')

df = df.drop(df[ df['波動率'] == 0 ].index)

volatility=[]
for i in df.values:
    volatility.append(i[1])

x = [[i] for i in np.array(volatility)]

model = KMeans(n_clusters = 5)
model.fit(x)



group_list=[]
for group in model.labels_ :
    group_list.append(group)

df['分群']=group_list
print(df)

df.to_csv('volatility_group.csv',encoding = 'utf-8-sig',index= False)



name=[]
for i in df.values:
    name.append(i[0])


plt.scatter( name,volatility,c=model.labels_)
plt.show()
