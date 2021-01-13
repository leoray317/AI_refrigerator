#進行數據分析之前常要引用的函式庫

import pandas as pd
import re

df = pd.read_csv('month_avg_price1.csv',encoding = 'utf-8-sig')

l=[]
for i in df.values:
    if re.search('..$',i[3]).group() != '市場':
        l.append(i)

l_df = pd.DataFrame(l,columns=['產品區域碼','月份','品名','地區','均價','均量'])

l_df.to_csv('month_not_market.csv',index = False,encoding='utf-8-sig')

'''
df_l_1 = pd.DataFrame(l,columns=['地區'])
df_l = df_l_1.drop_duplicates(['地區'])

df_l.to_csv('area.csv',index = False,encoding = 'utf-8-sig')

'''