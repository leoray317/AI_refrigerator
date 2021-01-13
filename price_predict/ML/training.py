# coding=gbk
import requests
from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
import time


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
url='https://amis.afa.gov.tw/fruit/FruitProdDayTransInfo.aspx'
cookies={'ASP.NET_SessionId':'tutwky4mwc4pj0mywhqzybvg'}

res=requests.get(url,headers=headers,cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')
#先取得隱藏欄位
view_state=soup.select('input#__VIEWSTATE')[0]['value']
event_validation=soup.select('input#__EVENTVALIDATION')[0]['value']

Product="全部產品"
ProductNo="ALL"

data={"ctl00$ScriptManager_Master":"ctl00$ScriptManager_Master|ctl00$contentPlaceHolder$btnQuery",
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__VIEWSTATE": view_state,
    "__VIEWSTATEGENERATOR": "A4896558",
    "__EVENTVALIDATION": event_validation,
    "ctl00$contentPlaceHolder$ucDateScope$rblDateScope": "D",
    "ctl00$contentPlaceHolder$ucSolarLunar$radlSolarLunar": "S",
    "ctl00$contentPlaceHolder$txtSTransDate": "108/06/10",
    "ctl00$contentPlaceHolder$txtETransDate": "109/06/10",
    "ctl00$contentPlaceHolder$txtMarket": "全部市場",
    "ctl00$contentPlaceHolder$hfldMarketNo": "ALL",
    "ctl00$contentPlaceHolder$txtProduct": Product,
    "ctl00$contentPlaceHolder$hfldProductNo": ProductNo,
    "ctl00$contentPlaceHolder$hfldProductType": "A",
    "__ASYNCPOST": "true",
    "ctl00$contentPlaceHolder$btnQuery": "下載Excel"}


res_post=requests.post(url,headers=headers,cookies=cookies,data=data)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://codepad.org')
 
# click radio button
python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
python_button.click()