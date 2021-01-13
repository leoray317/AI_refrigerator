import pandas as pd

df = pd.read_csv('how.csv',encoding='utf-8-sig')

df_new = df.drop_duplicates(['日期'])

df_new.to_csv('new_how.csv',encoding='utf-8-sig',index = False)
