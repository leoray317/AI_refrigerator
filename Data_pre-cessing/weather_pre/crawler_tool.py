import pandas as pd
import glob
import os
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError
import requests
from time import sleep
from os.path import isfile, join
from os import listdir


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}


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

def combined_csv(): #combine all dataframe in each data folder

    # list all folder name 
    county_path = r'.\data'
    counties = [f for f in listdir(county_path) ]

    for folder_name in counties:

        path = f'{county_path}\{folder_name}' # use your path
        
        all_files = glob.glob(path + "/*.csv")
        print(all_files)

        li = []

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)
    frame.to_csv(f'{folder_name}.csv', index=None)
class Date(object):
    ''' 
    傳入日期區間, 可以回傳包含 "日" or 未包含 "日"
        
        -> 包含日: str_day_range
        -> 未包含: str_month_range      
     '''
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date  = end_date
        self.str_day_range = self.__day_range
        self.str_month_range = self.__month_range    

    def __day_range(self):
        '''ex: '2019-01-01' -> 字串型態傳入'''
        
        DAY_RANGE =  pd.date_range(self.start_date, self.end_date).tolist()    
        STR_DAY_RANGE = [i.strftime("%Y-%m-%d") for i in DAY_RANGE]
        
        return STR_DAY_RANGE

    def __month_range(self):
        '''
        ex: '2019-01' -> 字串型態傳入
        dict.fromkeys remove duplicates
        '''
        MONTH_RANGE =  pd.date_range(self.start_date, self.end_date).tolist()    
        STR_MONTH_RANGE = [i.strftime("%Y-%m") for i in MONTH_RANGE]       
        STR_MONTH_RANGE = list(dict.fromkeys(STR_MONTH_RANGE)) 
        return STR_MONTH_RANGE
if __name__ == "__main__":
    a = Date('2019-01-01', '2019-12-31')
    print(a.str_day_range())
            