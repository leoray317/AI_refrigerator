import pandas as pd
import glob
import os
from os.path import isfile, join
from os import listdir
 
def merge():
    # list all folder name 
    county_path = r'./data'
    counties = [f for f in listdir(county_path) ]
    for i in counties:
        path = f"{county_path}/{i}"
        station_path_list = [f"{path}/{f}" for f in listdir(path) if isfile(join(path, f))]
        print(f"===============開始{i}")
        for z in station_path_list:
            #read csv
            df = pd.read_csv(z)
            # merge 
            #month_list = [str(i) for i in df['日期'].tolist()]
            #day_list = [str(j) for j in  df['觀測時間(day)'].tolist()]

            #print(month_list, day_list)

            #final_list= list()
            #for i, j in enumerate(day_list):
            #    a = f"{month_list[i]}-{j}"
            #    final_list.append(a)             
            #df = df.drop(['觀測時間(day)'], axis=1)
            df = df.drop(['日期'], axis=1)
            col = df.columns.tolist()
            col = [col[-1]] + col[:-1]
            df = df[col]
            print(z)
            df.to_csv(z,index=None,encoding='utf-8-sig')

        
def insert_city_station_name():       # 在全部資料夾裡的工作站分別全部加入工作站名、縣市名稱
    # config file path
    config_file_path= r'./config'
    config_csv_list = [f for f in listdir(config_file_path) ]
    i = 0
    for config_csv in config_csv_list:
        # get county name from config
        config_county = config_csv[:-4] # 縣市
        print("============================")
        print("正在處理: ",config_county)
        
        df = pd.read_csv(f"{config_file_path}/{config_csv}")
        
        # get station_name
        station_name_list = df.iloc[:,1].tolist()
        for station_name in station_name_list:
            print("站名: ", station_name.split(" ")[0])

            # data path
            data_path = r'./data'
            # enter county
            into_county_path = f"{data_path}/{config_county}"
            # read csv by station name
            station_path = f"{into_county_path}/{station_name}.csv"
            df_station = pd.read_csv(station_path)
            df_station.insert(1,"觀測站名", str(station_name.split(" ")[0])) # 先城市 在觀測站名
            df_station.insert(1,"縣市", str(config_county)) # 先城市 在觀測站名
            df_station.to_csv(station_path, index=None, encoding='utf-8-sig')

def combined_csv(): #combine all dataframe in each data folder

    # list all folder name 
    county_path = r'.\data'
    counties = [f for f in listdir(county_path) ]

    for folder_name in counties:
        print("==========================", folder_name)
        path = f'{county_path}\{folder_name}' # use your path
        
        all_files = glob.glob(path + "/*.csv")
        

        li = []

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            li.append(df)
        frame = pd.concat(li, axis=0, ignore_index=True)        
        frame.to_csv(f'./combined_data/{folder_name}.csv', index=None)

def drop_specific_cols(): 
    #read all csv in dir
    combine_data_path = r'./combined_data'
    counties = [f for f in listdir(combine_data_path) ]
    for county in counties:
        df_county = pd.read_excel(f"{combine_data_path}/{county}")
        # drop cols
        needed_cols = ["時間", "縣市","觀測站名","氣溫(℃)", "最低氣溫(℃)","相對溼度(%)", "風速(m/s)","降水量(mm)"]
        df_county = df_county.loc[:,needed_cols]
        df_county.to_csv(f"{combine_data_path}/{county}", index=None, encoding='utf-8-sig')
    
def all2xlsx():
    """
    把資料夾全部csv 轉為xlsx
    因為csv 太多問題
    """
    combine_data_path = r'./combined_data'
    counties = [f for f in listdir(combine_data_path) ]
    for county in counties:
        df_county = pd.read_csv(f"{combine_data_path}/{county}")
        df_county.to_excel(f'{county[:-4]}.xlsx', index=None, encoding="utf-8-sig")


if __name__ == "__main__":
    drop_specific_cols()
            