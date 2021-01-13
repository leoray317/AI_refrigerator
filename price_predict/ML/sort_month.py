import pandas as pd
import tqdm

df = pd.read_csv('final_day.csv',encoding='utf-8-sig')

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
    name_df = pd.DataFrame(name,columns=['產品區域碼','月份','產品碼','品名','地區碼','地區','均價','均量','時間','縣市','觀測站名','氣溫(℃)','最低氣溫(℃)','相對溼度(%)','風速(m/s)','降水量(mm)'])
    name_df_sort = name_df.sort_values(by =['月份'])
    name_list = name_df_sort.values


    for n in name_list:
        name_total.append(n)
        #print(n)


total_df = pd.DataFrame(name_total,columns=['產品區域碼','月份','產品碼','品名','地區碼','地區','均價','均量','時間','縣市','觀測站名','氣溫(℃)','最低氣溫(℃)','相對溼度(%)','風速(m/s)','降水量(mm)'])           
    
print(total_df)
#df_sort = df.sort_values(by=['產品區域碼'])



total_df.to_csv('final1_day.csv',index = False,encoding = 'utf-8-sig')

