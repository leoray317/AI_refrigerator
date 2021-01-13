from flask import Flask,jsonify,request,render_template,Response
import json
import requests
import shutil
import matplotlib.pyplot as plt
import datetime
from PIL import Image
import base64

app=Flask(__name__)

@app.route('/')
def hellFlask():
    result = {
        "name": "python",
        "url": "https://avatars0.githubusercontent.com/u/1525981?s=200&v=4"
    }
    return result


def img():
    # 下載圖片
    request_data = request.get_json()
    r = requests.get(request_data['url'], stream=True)
    try:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        filename = "./fullpageweb/get_img.jpg"
        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            f.write(r.content)
        print('成功下載圖檔: ', filename)
        """
        這邊呼叫 Yolov4 預測功能
        """

        # import時間使圖片名稱可加上時間
        today = datetime.datetime.today()
        time = today.strftime("%Y%m%d%H%M%S")

        # 使用pillow編輯圖片
        im = Image.open("./fullpageweb/get_img.jpg")
        width = 200
        height = 200
        nim = im.resize((width, height), Image.BILINEAR)
        nim4 = nim.transpose(Image.ROTATE_90)
        img_url = "./fullpageweb/static/fileout" + time + ".png"
        print("img_url:", img_url)
        nim4.save(img_url)


        outStr = '<img src="/static/fileout' + time + '.png">'
        print_img_url = img_url.split('/')[-1]
        print(print_img_url)
        print("outStr:", outStr)
        return print_img_url

    except Exception as e :
        print(e,"\n 下載失敗")


@app.route('/post', methods=['POST'])
def hellFlask_post():

    update_result = {
        "result": "python-new",
        "url": "http://127.0.0.1:5000/static/"+img()
    }
    return jsonify(update_result)

#加上'debug=True' 不須重新啟動即可更新資料
if __name__=='__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)