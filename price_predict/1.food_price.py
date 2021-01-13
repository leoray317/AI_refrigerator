import requests
from bs4 import BeautifulSoup
import lxml
import json
import pandas as pd
import tqdm
import time
from requests.exceptions import ConnectionError
from requests.exceptions import ReadTimeout


def requests_get(*args1, **args2): # 被鎖時會每60秒重複嘗試request 總共5次
    i = 5
    while i >= 0:
        try:
            return requests.get(*args1, **args2)
        except (ConnectionError, ReadTimeout) as error:
            print(error)
            print('retry one more time after 60s', i, 'times left')
            sleep(60)
        i -= 1
    return pd.DataFrame()


headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie':'_ga=GA1.3.1401094577.1591692355; _gid=GA1.3.1354790245.1591692355; ASP.NET_SessionId=mjlg2fy3glc5fmrg1fi4vfwy',
'Host': 'agridata.coa.gov.tw',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}


date = pd.date_range('2020-05-29','2020-06-01')
a= date.to_list()

total_list=[]
for i in tqdm.tqdm(a) :
    i = str(i).replace(' 00:00:00','').replace('-','.')
    i = i.split('.')
    i[0] = str(int(i[0])-1911)
    date_new = i[0]+'.'+i[1]+'.'+i[2]
    url='https://agridata.coa.gov.tw/api/v1/AgriProductsTransType/?End_time='+ date_new
    
    
    
    res = requests_get(url,headers = headers)
    soup = BeautifulSoup(res.text,'lxml')
    p = soup.find('p')
    
    context_json = json.loads(p.text)
    context = context_json['Data']
    
    for g in context:
        l=[]
        l.append(g['TransDate'])
        l.append(g['CropCode'])
        l.append(g['CropName'])
        l.append(g['MarketCode'])
        l.append(g['MarketName'])
        l.append(g['Upper_Price'])
        l.append(g['Middle_Price'])
        l.append(g['Lower_Price'])
        l.append(g['Avg_Price'])
        l.append(g['Trans_Quantity'])
        total_list.append(l)
        if l == []:
            print('沒資料')
            continue
    

df = pd.DataFrame(total_list,columns = ['日期','產品碼','產品名','市場碼','市場名','上價','中價','下價','平均價格','交易量'])

df.to_csv('total.csv',encoding='utf-8-sig')

