import pandas as pd

df = pd.read_csv('food_list.csv')



#只選擇台北且未休市之資料
tai=[]
for i in df.values:
    if i[5] == '台北二' and i[3] != '休市':
        tai.append(i)
    if i[5] == '台北一'and i[3] != '休市':
        tai.append(i)
    

df_tai = pd.DataFrame(tai)

##簡單化資料

#取得產品list
name=[]
for i in tai:
    #簡化name
    a = i[3].split('-')
    name.append(a[0])


df_tai[3] = name

#只取10個
l = ['青江白菜','蘆筍','奇異果','西瓜','草菇','溼香菇','火龍果','甘藍','熟筍','香蕉']
ten = []
for i in l:    
    for j in df_tai.values:
        if j[3] == i:
            ten.append([j[1],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10]])

df_ten = pd.DataFrame(ten,columns = ['日期','產品名','地區碼','市場名','上價','中價','下價','平均價格','交易量'])

#drop掉重複日期資料

df = df_ten.drop_duplicates(['日期','產品名'])
#照日期排序
name_total = []
for i in l:
    name = []
    for j in df.values:
        if j[1] == i :
            name.append(j)
    name_df = pd.DataFrame(name,columns=['日期','產品名','地區碼','市場名','上價','中價','下價','平均價格','交易量'])
    name_df_sort = name_df.sort_values(by =['日期'])
    name_list = name_df_sort.values


    for n in name_list:
        name_total.append(n)

df = pd.DataFrame(name_total,columns=['日期','產品名','地區碼','市場名','上價','中價','下價','平均價格','交易量'])

df.to_csv('2ten_food.csv',index= False,encoding='utf-8-sig')

