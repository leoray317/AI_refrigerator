import pandas as pd 
import datetime 
import tqdm

df = pd.read_csv('total_not_market.csv',encoding = 'utf-8-sig')

month = []
for i in df.values:
    a = i[1].split('.')
    datestring = str(int(a[0])+1911)+'/'+ a[1] + '/' + a[2]
    date = datetime.datetime.strptime(datestring, '%Y/%m/%d')
    date_month_back = date - datetime.timedelta(days=30)
    month.append(str(date_month_back.date()))

df['過去一個月'] = month

df = df.sort_values(['產品碼','地區碼'])


l=[]
for i in df.values:
    l.append([i[3],i[5]])


df_l_1 = pd.DataFrame(l,columns=['品名','地區'])
df_l = df_l_1.drop_duplicates(['品名','地區'])

name_total = []
for i in tqdm.tqdm(df_l.values):
    name = []
    for j in df.values:
        if j[3] == i[0] and j[5] == i[1]:
            name.append(j)
    name_df = pd.DataFrame(name,columns=['產品區域碼','月份','產品碼','品名','地區碼','地區','均價','均量','時間'])
    name_df_sort = name_df.sort_values(by =['月份'])
    name_list = name_df_sort.values


    for n in name_list:
        name_total.append(n)

total_df = pd.DataFrame(name_total,columns=['產品區域碼','月份','產品碼','品名','地區碼','地區','均價','均量','時間'])           
    
total_df.to_csv('total_unmarket_backmonth.csv',index= False,encoding='utf-8-sig')