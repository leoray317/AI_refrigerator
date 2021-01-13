import pandas as pd

df = pd.read_csv('total.csv',encoding='utf-8-sig')

df = df.drop(df[ df['產品名'] == '休市' ].index)
df = df.drop(df[ df['平均價格'] == 0 ].index)
df = df.drop(df[ df['交易量'] == 0 ].index)

df_product = df['產品名'].values

l=[]
for  i in df_product:
    t = i.split('-')[0]
    l.append(t.split('(')[0]) 

df['產品名'] = l

df.to_csv('total_same_name.csv',encoding = 'utf-8-sig',index = False)
