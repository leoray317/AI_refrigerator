import numpy as np
import pandas as pd


def muitple_days(path, days, file_name):
    """
    path = 要處理的csv路徑(路徑中至少包含2年以上資料)
    days = 在每條row中加入後幾天資料
    
    這邊預設改變一年資料
    也就是說import 的csv 有兩年資料, 會改變的rows 為前面一年的資料且只輸出前面一年的資料
    """    
    df = pd.read_csv(path)
    # deal with col names
    col = np.array(df.columns.tolist()[3:])
    final_col = list()

    for i in range(days): # the number in range depends on the day above! 
        final_col.append(col)

    final_col = [item for sublist in final_col for item in sublist]
    # DataFrame to np.array
    df_np = df.iloc[:,3:].to_numpy()
    
    # np numpy array decending
    df_np = df_np[::-1]
    
    # start deal with the np.array
    result = list()

    for i in range(len(df)):
        # depends on how many days wanna append 
        # the exmaple, here, appended by 5 days= 6 dyas info for a day
        result.append(np.append(df_np[i], df_np[i+1:i+days])) 
        
        # deal with the last few days by the next month info

    result = [i.tolist() for i in result[:365]] # default one year
    
    # list reverse back to acsending
    result.reverse()
    df_result = pd.DataFrame(result, columns=final_col)
    # deal with the date
    date = df.iloc[365:,0].tolist()
    df_result.insert(0, '日期',date)
    df_result.to_csv(f'{file_name}.csv', index=None, encoding='utf-8-sig')

if __name__ == "__main__":
    path = r'./竹子湖.csv'
    muitple_days(path, 50, "竹子湖改")