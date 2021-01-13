from flask import Flask
from flask import jsonify
import os
import json


img_path = "/pic/motion/lastsnap.jpg"
web_url="http://10.120.26.222:5000"

'''
with open ('/home/pi/pic/lists.json') as f:
    t = f.read()
    lists = json.loads(t)
'''

app = Flask(__name__,static_url_path='/pic',static_folder='/home/pi/pic')

@app.route('/return_pic')
def return_pic():
    out_str='<img src="'+img_path+'">'
    return(out_str)

@app.route('/snapshot')
def snapshot():
    os.system('bash /home/pi/pic/bin/snapshot.sh')
    a=os.popen('ls -t /home/pi/pic/motion/*.jpg').read()
    s=str(a).replace('/home/pi',web_url).split('\n')[0]
    url_js = json.dumps({"url":s})
    return url_js

@app.route('/pics')
def pics():    
    js=[]
    tmp={}
    a=os.popen('ls -t /home/pi/pic/motion/*.jpg').read()
    s=str(a).replace('/home/pi',web_url).split('\n')    
    for i in range(0,len(s[0:-1])):
        tmp.setdefault('pic%03d'%i,s[i])
        sorted(tmp.keys())    
    lists={'list':tmp}       
    return jsonify(lists)

if __name__ == '__main__':
    app.run(debug=True,host='10.120.26.222',port=5000)