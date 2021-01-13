import pandas as pd 

df = pd.read_csv('total_same_name.csv')

#for i in df.values:
#    print(i[1].split('.')[2])


food_area_list = []
for i in df.values:
    food_area_list.append([i[3],i[5]])

food_area_df = pd.DataFrame(food_area_list,columns = ['name','area'])

food_area_df = food_area_df.drop_duplicates(subset=['name','area'])

food_area = []
for i in food_area_df.values:
    food_area.append(i)

month = ['01']
#,'02','03','04','05','06','07','08','09','10','11','12']


month_avg_price = []
for t in month:
    for j in food_area:
        name = []
        code = []
        day_of_month_price = []
        area = []
        for i in df.values:
            if i[3]==j[0] and i[5]==j[1] :
                    #day_of_month_price = []
                    if i[1].split('.')[1] == t :
                        #print(i[1],i[3],i[5],i[6])
                        code.append(i[2])
                        name.append(i[3])
                        day_of_month_price.append(i[6])
                        area.append(i[5])
        print([area[0],t+'月',code[0],name[0],round(sum(day_of_month_price)/len(day_of_month_price),2)])
        month_avg_price.append([area[0],t+'月',code[0],name[0],round(sum(day_of_month_price)/len(day_of_month_price),2)])

print(pd.DataFrame(month_avg_price))
'''
month_df = pd.DataFrame(month_avg_price)
month_df.to_csv('month_avg_price.csv',encoding = 'utf-8-sig',index = False)
'''               
                    
            




