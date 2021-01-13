import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import datetime

def avg(c):
    a=sum(c)/len(c)
    return a
#移動平均
def movavg(num,a):
    p=[]
    for i in range(num):
        p.append(a[i])

    for j in range(len(a)-num):
        t=[]
        for k in  range(num):
            t.append(a[k+j])
        p.append(round(avg(t),2))
    return p

df = pd.read_csv('2ten_food.csv',encoding = 'utf-8-sig')

#建立時間欄位
a=[]
b=[]
for i in df.values:
    date = i[0].split('.')
    #print(str(int(date[0])+1911))
    year = str(int(date[0])+1911)+'/'+str("%02d" % int(date[1]))+'/'+str("%02d" % int(date[2]))
    lasttime = datetime.datetime.strptime(year,'%Y/%m/%d') - datetime.timedelta(days=30)
    last_time = lasttime.strftime('%Y/%m/%d')
    
    a.append(year)
    b.append(last_time)


df['西元日期'] = a
df['時間'] = b


df_104 =pd.read_csv('台北104.csv',encoding = 'big5')


time=[]
for i in df_104.values:
    date = i[0].split('/')
    print()
    year = str(int(date[0]))+'/'+str("%02d" % int(date[1]))+'/'+str("%02d" % int(date[2]))
    time.append(year)

df_104['時間'] = time

#合併表格
res= pd.merge(df, df_104, on=['時間', '地區碼'])


res = res.sort_values(by = '產品名')


#先存原始
#res.to_csv('3.final.csv',index= False,encoding='utf-8-sig')


#增加移動平均之欄位
l=['青江白菜','蘆筍','奇異果','西瓜','草菇','溼香菇','火龍果','甘藍','熟筍','香蕉']

final = []
for name in l:
    food=[]
    for i in res.values:
        if i[1] == name:
            food.append([i[9],i[1],i[7],i[4],i[5],i[6],i[8],i[13],i[14],i[15],i[16],i[17]])
    df = pd.DataFrame(food,columns=['日期','產品名','平均價格','上價','中價','下價','交易量','月前氣溫','月前最低氣溫','月前相對溼度','月前風速','月前降水量'])
    
    df = df.sort_values(by = '日期')

    df = df.fillna(value=0)
    print(df)
    avg_price = []
    up_price = []
    mid_price = []
    low_price = []
    vol = []
    temp = []
    low_temp = []
    wet = []
    wind = [] 
    rain = []
    for i in df.values:
        avg_price.append(i[2])
        up_price.append(i[3])
        mid_price.append(i[4])
        low_price.append(i[5])
        vol.append(i[6])
        temp.append(i[7])
        low_temp.append(i[8])
        wet.append(i[9])
        wind.append(i[10])
        if i[11] == 'T' :
            a = i[11].replace('T','0')
            rain.append(float(a))
        else:
            rain.append(float(i[11]))

    df['月前降水量'] = rain
    
    df['前一日均價'] = movavg(1,avg_price)
    df['五日移動平均均價'] = movavg(5,avg_price)
    df['十日移動平均均價'] = movavg(10,avg_price)
    df['二十日移動平均均價'] = movavg(20,avg_price)
    df['五十日移動平均均價'] = movavg(50,avg_price)
    df['百日移動平均均價'] = movavg(100,avg_price)

    df['前一日上價'] = movavg(1,up_price)
    df['五日移動平均上價'] = movavg(5,up_price)
    df['十日移動平均上價'] = movavg(10,up_price)
    df['二十日移動平均上價'] = movavg(20,up_price)
    df['五十日移動平均上價'] = movavg(50,up_price)
    df['百日移動平均上價'] = movavg(100,up_price)

    df['前一日中價'] = movavg(1,mid_price)
    df['五日移動平均中價'] = movavg(5,mid_price)
    df['十日移動平均中價'] = movavg(10,mid_price)
    df['二十日移動平均中價'] = movavg(20,mid_price)
    df['五十日移動平均中價'] = movavg(50,mid_price)
    df['百日移動平均中價'] = movavg(100,mid_price)

    df['前一日下價'] = movavg(1,low_price)
    df['五日移動平均下價'] = movavg(5,low_price)
    df['十日移動平均下價'] = movavg(10,low_price)
    df['二十日移動平均下價'] = movavg(20,low_price)
    df['五十日移動平均下價'] = movavg(50,low_price)
    df['百日移動平均下價'] = movavg(100,low_price)

    df['前一日量'] = movavg(1,vol)
    df['五日移動平均量'] = movavg(5,vol)
    df['十日移動平均量'] = movavg(10,vol)
    df['二十日移動平均量'] = movavg(20,vol)
    df['五十日移動平均量'] = movavg(50,vol)
    df['百日移動平均量'] = movavg(100,vol)

    df['月前五日移動平均溫'] = movavg(5,temp)
    df['月前十日移動平均溫'] = movavg(10,temp)
    df['月前二十日移動平均溫'] = movavg(20,temp)
    df['月前五十日移動平均溫'] = movavg(50,temp)
    df['月前百日移動平均溫'] = movavg(100,temp)

    df['月前五日移動平均低溫'] = movavg(5,low_temp)
    df['月前十日移動平均低溫'] = movavg(10,low_temp)
    df['月前二十日移動平均低溫'] = movavg(20,low_temp)
    df['月前五十日移動平均低溫'] = movavg(50,low_temp)
    df['月前百日移動平均低溫'] = movavg(100,low_temp)

    df['月前五日移動平均濕度'] = movavg(5,wet)
    df['月前十日移動平均濕度'] = movavg(10,wet)
    df['月前二十日移動平均濕度'] = movavg(20,wet)
    df['月前五十日移動平均濕度'] = movavg(50,wet)
    df['月前百日移動平均濕度'] = movavg(100,wet)

    df['月前五日移動平均風速'] = movavg(5,wind)
    df['月前十日移動平均風速'] = movavg(10,wind)
    df['月前二十日移動平均風速'] = movavg(20,wind)
    df['月前五十日移動平均風速'] = movavg(50,wind)
    df['月前百日移動平均風速'] = movavg(100,wind)

    df['月前五日移動平均降水'] = movavg(5,rain)
    df['月前十日移動平均降水'] = movavg(10,rain)
    df['月前二十日移動平均降水'] = movavg(20,rain)
    df['月前五十日移動平均降水'] = movavg(50,rain)
    df['月前百日移動平均降水'] = movavg(100,rain)

    
    #print(df)
    for i in df.values:
        if i[11] == 'T':
            print(i[11])
        final.append(i)

df = pd.DataFrame(final,columns=['日期','產品名','平均價格','上價','中價','下價','交易量',\
    '月前氣溫','月前最低氣溫','月前相對溼度','月前風速','月前降水量',\
    '前日價格','五日移動平均價','十日移動平均價','二十日移動平均價','五十日移動平均價','百日移動平均價',\
    '前日上價','五日移動平均上價','十日移動平均上價','二十日移動平均上價','五十日移動平均上價','百日移動平均上價',\
    '前日中價','五日移動平均中價','十日移動平均中價','二十日移動平均中價','五十日移動平均中價','百日移動平均中價',\
    '前日下價','五日移動平均下價','十日移動平均下價','二十日移動平均下價','五十日移動平均下價','百日移動平均下價',\
    '前日量','五日移動平均量','十日移動平均量','二十日移動平均量','五十日移動平均量','百日移動平均量',\
    '月前五日移動平均氣溫','月前十日移動平均溫','月前二十日移動平均溫','月前五十日移動平均溫','月前百日移動平均溫',\
    '月前五日移動平均低溫','月前十日移動平均低溫','月前二十日移動平均低溫','月前五十日移動平均低溫','月前百日移動平均低溫',\
    '月前五日移動平均濕度','月前十日移動平均濕度','月前二十日移動平均濕度','月前五十日移動平均濕度','月前百日移動平均濕度',\
    '月前五日移動平均風速','月前十日移動平均風速','月前二十日移動平均風速','月前五十日移動平均風速','月前百日移動平均風速',\
    '月前五日移動平均降水','月前十日移動平均降水','月前二十日移動平均降水','月前五十日移動平均降水','月前百日移動平均降水'])



df.to_csv('3.final.csv',index= False,encoding='utf-8-sig')

