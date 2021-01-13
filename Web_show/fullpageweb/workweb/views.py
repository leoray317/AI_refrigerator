from django.shortcuts import render,HttpResponse
import json
import requests
import jsonpath
from fullpageweb import settings
from django.views.generic import View
from django.http import JsonResponse
import random
import pandas as pd
import base64
import time
from bs4 import BeautifulSoup

import numpy as np
import pymysql.cursors
from sqlalchemy import create_engine
from sqlalchemy.types import CHAR,INT
import datetime
import line_notify

def pagelist(request):
    temp={}
    if request.method == 'POST':
        if request.POST['showone']:
            temp['gotit'] = 1
    return render(request,'workweb/fullpage.html', temp)

# =============================================================================

# webcam路徑
def photo(request):

    #webcam的api
    url = "http://10.120.26.222:5000/snapshot"
    print(url)
    #測試用flask api，需開啟自己的api
    #url = "http://127.0.0.1:5000/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url, headers=headers)  # 取得影像的api，獲得影像擷取的url
    json_data = json.loads(res.text)   # flask api 回傳的資料
    print("第一次:", json_data)
    return JsonResponse(json_data)

# 預測路徑
def photo_post(request):

    json_photo = photo(request)
    json_photo_post = json.loads(json_photo.content)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }

    #測試用lask api，需開啟自己的api
    url_post = "http://127.0.0.1:5000/post"

    #遠端預測機台
    #url_post = "http://10.120.26.240:5000/post"

    res_post = requests.post(url_post, headers=headers, json=json_photo_post)  # 使用回傳的資料進行另一網路的request post，資料以json格式傳送
    json_data_post = json.loads(res_post.text)  # 得到post後傳回的資料(字串格式)用loads轉字典

    return JsonResponse(json_data_post)  # 同等於return HttpResponse(json.dumps(json_data))

# =============================================================================

def food_table(*args, **kwargs):
    labels = ["青江白菜","蘆筍","奇異果","西瓜","草菇","溼香菇","火龍果","甘藍","竹筍","香蕉",]
    return labels


def show_food(request, *args, **kwargs):
    data = [1, 2, 7, 4, 5, 6, 0, 8, 5, 2]
    # random.shuffle(data)
    labels = food_table()
    content = {
        'data': data,
        'labels': labels,
    }
    return JsonResponse(content)

# =============================================================================

# 營養素種類
def food_nutrients_table(*args, **kwargs):
    labels = ["熱量(kcal)", "鈣(mg)", "鎂(mg)", "鐵(mg)", "鋅(mg)", "磷(mg)", "維生素A(ug RE)", "維生素E(mg)", "維生素B1(mg)", "維生素B2(mg)", "維生素B6(mg)", "維生素C(mg)"]
    return labels


# 標準營養素
def get_data(request, *args, **kwargs):
    df = pd.read_csv("./食物營養素.csv", index_col="name")  # 讀取csv並指定name欄位為索引值
    df_json = df.to_json(orient="values", force_ascii=False)  # 將dataframe轉為json格式
    json_data = json.loads(df_json)
    labels = food_nutrients_table()  # 載入營養素種類
    data_per = [i/i*100 for i in json_data[10]]
    content = {
        'data': data_per,
        'labels': labels,
    }
    return JsonResponse(content)



# def lack_nut(data):
#     print('lack_nut_1:',data['lack_data'])
#     print('lack_nut_2:',data['labels'])
#     return 

# 目前營養素
def get_data1(request):
    df = pd.read_csv("./食物營養素.csv",index_col="name")  # 讀取csv並指定name欄位為索引值
    df_json = df.to_json(orient="values",force_ascii=False)  # 將dataframe轉為json格式
    json_data = json.loads(df_json)
    labels = food_nutrients_table()

    # 判斷年齡層
    if request.is_ajax() and request.method == "POST":
        name = request.POST.get("name")
        if name == "7-9":
            # food_num = [0.4, 6.25, 1.45, 0.04, 1, 1, 0.33, 0.07, 0.33, 1]
            food_num = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            
            # 考慮水果數量，將現有營養素串列與建議營養素串列相除得到百分比(目前值/建議值)
            data = [[(a / b) * food_num[i] * 100 for a, b in zip(json_data[i], json_data[10])] for i in range(10)]

            lack_data=[100-data[0][j] for j in range(len(data[0]))]
            
            #print("data",data[0])
            #print("lack-data",lack_data)

            content = {
                'data': data,
                'labels': labels,
            }
            
            return JsonResponse(content)

        elif name == "19-30":
            # food_num = [0.4, 6.25, 1.45, 0.04, 1, 1, 0.33, 0.07, 0.33, 1]
            food_num = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            data = []
            for i in range(10):
                data_percentage = [(a / b) * food_num[i] * 100 for a, b in
                                   zip(json_data[i], json_data[11])]
                data.append(data_percentage)

            lack_data=[100-data[0][j] for j in range(len(data[0]))]

            content = {
                'data': data,
                'labels': labels,
            }
            
            return JsonResponse(content)

        else:
            print("no data")

# 資料庫儲存
def sql(dict_data):
    df = pd.DataFrame(columns=["date","青江白菜","蘆筍","奇異果","西瓜","草菇","溼香菇","火龍果","甘藍","竹筍","香蕉",])
    try:
        # 連接資料庫
        db_data = 'mysql+pymysql://root:123456@localhost:3306/fullpagedb?charset=utf8mb4'
        engine = create_engine(db_data)
        print("成功連結")

        # 插入資料
        df = df.append(dict_data, ignore_index=True)
        df.to_sql(name = 'fruit_table',  
            con = engine,
            if_exists = 'append',
            index = False,
        )
        print("成功insert")
    except Exception as ex:
        print("問題發生:",ex)
    #print(df)

# 傳至line notify
def line_note(dict_data):
    # 取出value為非0值的key
    data_kv = {k:v for k,v in dict_data.items() if v!='0'}
    data_time = data_kv['date']

    # 刪除時間欄位
    del data_kv['date']

    # 將取用的蔬果加入換行符號，line排版用
    data_item=[item[0]+str(eval(item[1])*100)+'g' for item in data_kv.items()]
    pri_list ="\n".join(data_item)

    # 向line notify 推撥
    n_text='\n時間 : '+str(data_time)+'\n已取用 :\n'+ pri_list
    line_notify.lineNotifyMessage(n_text)
    print('update to line')
    


# 缺乏營養素
def lack_nut(dict_data):
    
    # 載入csv
    df = pd.read_csv("./食物營養素.csv", index_col="name") 
    # df按照列轉json
    df_json = df.to_json(orient="values", force_ascii=False)
    json_data = json.loads(df_json)
    #print(json_data)
    # 載入營養素欄位
    labels = df.columns[1:12]
    
    #得到取出的蔬果數量並轉list
    del dict_data['date']
    food_num = list(dict_data.values())
    #print('food_num',food_num)

    # 標準值乘上取出的數量
    ans_list=[]
    for i in range(len(food_num)):
        ans = ans_list.append([j*int(food_num[i]) for j in json_data[i]])
    #print(ans_list)

    # list內相加
    ans_sum = np.sum([ans_list[i] for i in range(10)],axis=0)
    
    # list相減(與標準的差值)
    delt = [x-y for x,y in zip(ans_sum,json_data[10])]

    # 推薦蔬果
    sug_list = ['青江白菜','火龍果','草菇','竹筍','草菇','青江白菜','竹筍','蘆筍','草菇','香蕉','香蕉']

    # 推薦列表
    lack_list = []
    need_list = []
    for i in range(10):
        if delt[i]<0:
            lack_list.append(labels[i])
            need_list.append(sug_list[i])
    print(lack_list)
    print(need_list)
    data_json = {
        'lack_list':lack_list,
        'need_list':need_list
    }
    return data_json



# 傳輸資料 & 計算營養數 
def get_num(request):
    if request.is_ajax() and request.method == "POST":
        dict_data = request.POST.get("dict")
        print(json.loads(dict_data))
        # 匯入sql
        sql(json.loads(dict_data))

        # line通知
        line_note(json.loads(dict_data))

        # # 計算營養數
        a = lack_nut(json.loads(dict_data))

    return  JsonResponse(a)
 


# =============================================================================

# 預測價格

#遠端預測機台
url_post = "http://10.120.26.19:5000/price"


#測試用lask api，需開啟自己的api
# url_post = "http://localhost:5000/price"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }


def price_pre(request):
    if request.is_ajax() and request.method == "POST":
        name = request.POST.get("name")
        print(name)
        furit_list=["a","b","c","d","e","f","g","h","i","j"]  #設定水果list

        # 若post進來的水果有在list內則取出該水果代入
        if name in furit_list:           
            data={"name":name}
            res_post = requests.post(url_post, headers=headers, json=data)
            json_data_post = json.loads(res_post.text)
            print(json_data_post)
            return JsonResponse(json_data_post)






















