from flask import Flask, jsonify, request, render_template, Response
import json
import requests
import shutil
import matplotlib.pyplot as plt
import datetime
from PIL import Image
import base64

app = Flask(__name__)


@app.route('/')
def hellFlask():
    result = {
        "name": "python",
        "url": "https://github.com/comet-602/img/blob/master/webimg/fruit.jpg?raw=true"
    }
    return result


def img():
    # 下載圖片
    request_data = request.get_json()
    r = requests.get(request_data['url'], stream=True)
    try:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        filename = "get_img.jpg"
        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            f.write(r.content)
        print('成功下載圖檔: ', filename)

        # 執行功能，這邊為轉圖片
        # import時間使圖片名稱可加上時間
        today = datetime.datetime.today()
        time = today.strftime("%Y%m%d%H%M%S")

        # 使用pillow編輯圖片
        im = Image.open("get_img.jpg")
        width = 200
        height = 200
        nim = im.resize((width, height), Image.BILINEAR)
        nim4 = nim.transpose(Image.ROTATE_90)
        img_url = "./static/fileout" + time + ".png"
        print("img_url:", img_url)
        nim4.save(img_url)

        outStr = '<img src="/static/fileout' + time + '.png">'
        print_img_url = img_url.split('/')[-1]
        print(print_img_url)
        print("outStr:", outStr)
        return print_img_url

    except Exception as e:
        print(e, "\n 下載失敗")


@app.route('/post', methods=['POST'])
def hellFlask_post():
    update_result = {
        "result": "python-new",
        "url": "http://127.0.0.1:5000/static/"+img()
    }
    print(update_result)
    return jsonify(update_result)


def price_pre():

    if request.method == "POST":
        data = request.get_json()
        name = data['name']

        if name == "a":
            content = {
                'price1': "price_a1",
                'price2': "price_a2",
                'price3': "price_a3",
                'pre_img_url': "./static/img/1.png",
            }
            return jsonify(content)

        elif name == "b":
            content = {
                'price1': "price_b1",
                'price2': "price_b2",
                'price3': "price_b3",
                'pre_img_url': "./static/img/2.png",
            }
            return jsonify(content)

        elif name == "c":
            content = {
                'price1': "price_c1",
                'price2': "price_c2",
                'price3': "price_c3",
                'pre_img_url': "./static/img/3.png",
            }
            return jsonify(content)

        elif name == "d":
            content = {
                'price1': "price_d1",
                'price2': "price_d2",
                'price3': "price_d3",
                'pre_img_url': "./static/img/4.png",
            }
            return jsonify(content)

        elif name == "e":
            content = {
                'price1': "price_e1",
                'price2': "price_e2",
                'price3': "price_e3",
                'pre_img_url': "./static/img/5.png",
            }
            return jsonify(content)

        elif name == "f":
            content = {
                'price1': "price_f1",
                'price2': "price_f2",
                'price3': "price_f3",
                'pre_img_url': "./static/img/6.png",
            }
            return jsonify(content)

        elif name == "g":
            content = {
                'price1': "price_g1",
                'price2': "price_g2",
                'price3': "price_g3",
                'pre_img_url': "./static/img/7.png",
            }
            return jsonify(content)

        elif name == "h":
            content = {
                'price1': "price_h1",
                'price2': "price_h2",
                'price3': "price_h3",
                'pre_img_url': "./static/img/8.png",
            }
            return jsonify(content)

        elif name == "i":
            content = {
                'price1': "price_i1",
                'price2': "price_i2",
                'price3': "price_i3",
                'pre_img_url': "./static/img/9.png",
            }
            return jsonify(content)

        elif name == "j":
            content = {
                'price1': "price_j1",
                'price2': "price_j2",
                'price3': "price_j3",
                'pre_img_url': "./static/img/10.png",
            }
            return jsonify(content)


@app.route('/price', methods=['POST'])
def price_pre_post():
    ss = price_pre()
    print(ss)
    return ss


# 加上'debug=True' 不須重新啟動即可更新資料
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
