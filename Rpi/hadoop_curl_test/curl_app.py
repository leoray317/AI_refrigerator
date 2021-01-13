
import base64
from flask import request
from flask import Flask
import os
 
app=Flask(__name__)
 

@app.route("/photo", methods=['POST'])
def get_frame():
    
    upload_file = request.files['file']
    
    file_name = upload_file.filename
    
    file_path=r'E:/project/hadoop/data/'
    if upload_file:
        # 地址拼接
        file_paths = os.path.join(file_path, file_name)
        # 保存接收的图片到桌面
        upload_file.save(file_paths)
        # 随便打开一张其他图片作为结果返回，
        #with open(r'C:/Users/Administrator/Desktop/1001.jpg', 'rb') as f:
            # res = base64.b64encode(f.read())
        str="OK\n"
        return str
 
 
 
if __name__ == "__main__":
    app.run(debug=True,host='10.120.26.22', port=5000)