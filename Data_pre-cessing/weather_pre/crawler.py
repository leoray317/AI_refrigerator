from tqdm import tqdm
from time import sleep
from bs4 import BeautifulSoup
import requests
import lxml
from urllib.parse import quote,unquote
import pandas as pd
from datetime import date,datetime
from missing_data_process import data_cleaning
import os
from crawler_tool import requests_get, combined_csv, Date, headers

station_path = ""
df_station = ""
counter = 0

def df2df_quote():
    ''' [[<station_name1>, <station_id1>], [<station_name2>, <station_id2>], ...] '''
    result = []
    STNAMES = df_station.iloc[:,1]
    QUOTE_STNAMES  = [quote(quote(i.split()[0])) for i in STNAMES]
    STATION_IDS = df_station.iloc[:,0].tolist()
    
    for i,j in enumerate(STATION_IDS):
        a = [j, QUOTE_STNAMES[i]]
        result.append(a)
    return result

def crawler(county, station, stname, datepicker): #stname
    global headers, counter
    dir_path = r"./data"
    if os.path.isdir(dir_path) is False:
        os.mkdir(dir_path)
    county_path = f'./data/{county}'
    if os.path.isdir(county_path) is False:
        os.mkdir(county_path)
    #print(unquote(unquote("%25E8%2587%25BA%25E5%258C%2597")))
    #print(station,unquote(unquote(stname)), datepicker)
    url = f'https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station={station}&stname={stname}&datepicker={datepicker}'
            
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    res = requests_get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    table_rows = soup.select('table')[1].find_all('tr',attrs={'class':'second_tr'})

    col_name = [] 
    i=0
    # 爬欄位名稱 list 0 為中文 1為英文
    for tr in table_rows:
        th = tr.find_all('th')
        row = [tr.text.strip() for tr in th if tr.text.strip()]
        if row and i >= 0:
            col_name.append(row)
        i += 1
    # 爬內容
    table_rows = soup.select('table')[1].find_all('tr')
    result = []
    i = 0
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        if row and i >= 3:
            result.append(row)
        i += 1
    
    df1 = pd.DataFrame(result)      
    df1 = pd.DataFrame(result, columns=col_name[0])    
    df1.insert(1,"觀測站名", str(unquote(unquote(stname)))) # 先城市 在觀測站名
    df1.insert(1,"縣市", str(county)) # 先城市 在觀測站名
    df1.insert(0, '日期', datepicker)
    # merge 
    month_list = [str(i) for i in df1['日期'].tolist()]
    day_list = [str(j) for j in  df1['觀測時間(day)'].tolist()]

    #print(month_list, day_list)

    final_list= list()
    for i, j in enumerate(day_list):
        a = f"{month_list[i]}-{j}"
        final_list.append(a)             
    df1 = df1.drop(['觀測時間(day)'], axis=1)
    df1 = df1.drop(['日期'], axis=1)
    #col = df1.columns.tolist()
    #col = [col[-1]] + col[:-1]
    #df1 = df1[col]
    df1.insert(0,'時間', final_list)
    needed_cols = ["時間", "縣市","觀測站名","氣溫(℃)", "最低氣溫(℃)","相對溼度(%)", "風速(m/s)","降水量(mm)"]
    df1 = df1.loc[:,needed_cols]
    df1= data_cleaning(df1, str(county))
    #print(df1)

    
    file_name = f'{county_path}/{unquote(unquote(stname))}.csv'
    
    if counter == 0 and os.path.isfile(file_name) is False:      
        df1.to_csv(file_name, encoding='utf-8-sig', index=None)
        counter+=1
    else:
        df1.to_csv(file_name , encoding='utf-8-sig', mode='a', header=False, index=None)
        counter+=1
    

def main():
    global counter, station_path, df_station
    # get all counties
    from os.path import isfile, join
    from os import listdir
    county_path = r'./config'
    counties = [f for f in listdir(county_path) if isfile(join(county_path,f))]
    counties = [i.replace(".csv", "") for i in counties]
    completed = os.listdir('./data')
    for k in counties:
        #if k not in completed:
        station_path = f'./config/{k}.csv'
        df_station = pd.read_csv(station_path)

        station_detail = df2df_quote()       
        days = Date('2005-01-01','2020-06-12').str_month_range()
        
        for j in range(len(station_detail)):
            sleep(1)
            counter = 0
            for i in range(len(days)):
            
            
                print("========================================", counter+1)
                print("日期: ", days[i])
                print("城市: ", k)
                print("爬取: ", station_detail[j][0], unquote(unquote(station_detail[j][1])))
                crawler(k,station_detail[j][0], station_detail[j][1], days[i])
                sleep(0.3)        
            sleep(3)    
        sleep(10) # 爬完一個城市 sleep 10 secs    



if __name__ == "__main__":
    main()