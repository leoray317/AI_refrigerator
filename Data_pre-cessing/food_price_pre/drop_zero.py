import pandas as pd

df = pd.read_csv('total_same_name.csv',encoding='utf-8-sig')


df = df.drop(df[ df['交易量'] == 0 ].index)

df.to_csv('total_same_name.csv',encoding = 'utf-8-sig',index = False)