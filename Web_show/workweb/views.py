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

def pagelist(request):
    temp={}
    if request.method == 'POST':
        if request.POST['showone']:
            temp['gotit'] = 1
    return render(request,'workweb/fullpage.html', temp)


def get(request):
    return render(request, 'workweb/fullpage.html')


def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a)+int(b)
    return HttpResponse(str(c))


def text(request):
    a=5
    b=21
    c=a+b
    return HttpResponse(c)
# =============================================================================


def photo(request):
    url = "http://127.0.0.1:5000/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
    res = requests.get(url, headers=headers)  # 取得影像的api，獲得影像擷取的url
    json_data = json.loads(res.text)   # flask api 回傳的資料
    print("第一次:", json_data)
    return JsonResponse(json_data)


def photo_post(request):

    json_photo = photo(request)
    json_photo_post = json.loads(json_photo.content)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

    url_post = "http://127.0.0.1:5000/post"
    res_post = requests.post(url_post, headers=headers, json=json_photo_post)  # 使用回傳的資料進行另一網路的request post，資料以json格式傳送
    json_data_post = json.loads(res_post.text)  # 得到post後傳回的資料(字串格式)用loads轉字典
    print(json_photo_post)

    return JsonResponse(json_data_post)  # 同等於return HttpResponse(json.dumps(json_data))





# =============================================================================

# 影像連結用
def web_video_url(request):
    # url = "http://10.120.26.222:5000/pic/motion/lastsnap.jpg"
    url = "http://10.120.26.222:5000/snapshot"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}
    res = requests.get(url, headers=headers)
    json_data = json.loads(res.text)
    return HttpResponse(json.dumps(json_data))

# =============================================================================


def web_img_url(request):
        # url="https://jsonplaceholder.typicode.com/posts/42"
    # url = "http://127.0.0.1:8080/fooddata/?format=json"
    url = "http://localhost:5000/avengers/all"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}
    res = requests.get(url, headers=headers)
    json_data = json.loads(res.text)
    return HttpResponse(json.dumps(json_data))
# =============================================================================


def food_table(*args, **kwargs):
    labels = ["青江白菜","蘆筍","奇異果","西瓜","草菇","溼香菇","火龍果","甘藍","竹筍","香蕉",]
    return labels


def show_food(request, *args, **kwargs):
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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


# 目前營養素
def get_data1(request):
    df = pd.read_csv("./食物營養素.csv",index_col="name")  # 讀取csv並指定name欄位為索引值
    df_json = df.to_json(orient="values",force_ascii=False)  # 將dataframe轉為json格式
    json_data = json.loads(df_json)
    print("json_data:",json_data)
    labels = food_nutrients_table()

    if request.is_ajax() and request.method == "POST":
        name = request.POST.get("name")
        if name == "7-9":
            # food_num = [0.4, 6.25, 1.45, 0.04, 1, 1, 0.33, 0.07, 0.33, 1]
            food_num = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            data = []
            for i in range(10):
                data_percentage = [(a / b) * food_num[i] * 100 for a, b in
                                   zip(json_data[i], json_data[10])]  # 考慮水果數量，將現有營養素串列與建議營養素串列相除得到百分比(目前值/建議值)
                data.append(data_percentage)

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

            content = {
                'data': data,
                'labels': labels,
            }
            return JsonResponse(content)

        else:
            print("no data")
    if request.method == "GET":
        return print("It's get")

# =============================================================================

