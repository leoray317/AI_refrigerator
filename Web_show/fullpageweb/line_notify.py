import requests
import _line_notify_token

def lineNotifyMessage(msg):
    headers = {
        "Authorization": "Bearer " + _line_notify_token.line_tok(), # 權杖，Bearer 的空格不要刪掉呦
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    
    # Post 封包出去給 Line Notify
    r = requests.post(
        "https://notify-api.line.me/api/notify",
        headers=headers, 
        params=payload)
    return r.status_code



if __name__ == '__main__':
    #message = "test1"   
    lineNotifyMessage()


# result = lineNotifyMessage(message)
# print(result) # 印一下回傳代碼

            

