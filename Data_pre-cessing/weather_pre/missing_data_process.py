import pandas as pd
from os import listdir
import os

combined_file_path= r'./combined_data'

def get_all_csv():
    global combined_file_path    
    return [f for f in listdir(combined_file_path) ]


def data_cleaning(df, county_name):
    # read csv     
    df = df
    # get all cols 
    all_cols = df.columns
    except_cols = ['時間', '縣市','觀測站名']
    test_cols = [i for i in all_cols if i not in except_cols]
    
    print(f"===============start testing cols of {county_name} county")

    for index_test_col in range(len(test_cols)):
        print(f"testing: {test_cols[index_test_col]}")
        # get column to list
        
        test_list = df[test_cols[index_test_col]].tolist()
        
        # get all keys and values and get positions which are str to a list
        _temp= dict()
        str_positions = list()

        for i, j in enumerate(test_list):
            try:
                _temp[i] = float(j)
            except:
                _temp[i] = str(j)
                str_positions.append(i)
        print(f"we got {len(str_positions)} strings in {test_cols[index_test_col]} ")
        #print(str_positions)
        if len(str_positions) !=0:
            
            position_range = [i for i in range(-3,4) if i!=0]
            
            #print("get str_positions !: ", str_positions)
            for str_position in str_positions:
                # get the key range from str_position AND get the value from key range               
                temp_values=[_temp[i] for i in [f+str_position for f in position_range if f+str_position>0 and f+str_position<len(df)]]
                
                try: # if three positions above and below are numeric
                    _temp[str_position] = round(sum(temp_values)/len(temp_values),1)                    
                except:
                    try: # try three positions abaove or below:
                        for n in range(3,0,-1):
                            try:
                                if round(sum(temp_values[:n])/len(temp_values[:n]),1):
                                    _temp[str_position] = round(sum(temp_values[:n])/len(temp_values[:n]),1)
                                else:
                                    pass
                            except:
                                _temp[str_position] ='nan'      
                    except:
                        _temp[str_position] ='nan'      

            

        
        df = df.drop(columns=[test_cols[index_test_col]])
        df.insert(index_test_col+3,test_cols[index_test_col], list(_temp.values())) 
    return df
    #df.to_csv(f"./cleaned_data/{county_name}", encoding='utf-8-sig', index=None)        
                          
def main():        
    global combined_file_path
    counties_list = get_all_csv()
    # mkdir if checked data not exists
    combined_data_path = r'./combined_data'
    if os.path.isdir(combined_data_path) is False:
        os.mkdir(combined_data_path)

    for path in counties_list:  
        combined_csv_path = f'{combined_file_path}/{path}'
        data_cleaning(combined_csv_path,path )
        print("done")
        
    
if __name__ == "__main__":
    main()