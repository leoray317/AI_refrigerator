from sklearn import datasets   #數據庫
from sklearn.cluster import KMeans #訓練方式
from sklearn import preprocessing
import pandas as pd
import numpy as np
from matplotlib import pyplot  as plt
import seaborn as sns

df = pd.read_csv('total_same_name.csv',encoding='utf-8-sig')


price=[]
volumn=[]
time=[]
for i in df.values:
    if i[3] == '草莓' and i[5] == '台北二':
        price.append(i[6])
        volumn.append(i[7])
        time.append(i[1])

x_price = preprocessing.scale(price)
x_volumn = preprocessing.scale(volumn)


#sns.distplot(x_volumn, hist=True, kde=True)
#sns.distplot(x_price, hist=True, kde=True)


#plt.hist(x_volumn, rwidth=0.5, bins=30, color='r')
#plt.hist(x_price, rwidth=0.5, bins=30, color='b')



#plt.boxplot(x_volumn)
#plt.boxplot(x_price)
plt.plot(time,x_price, color='red')
plt.plot(time,x_volumn, '--', color='blue')

plt.show()