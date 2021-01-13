from tqdm import tqdm
from time import sleep
from bs4 import BeautifulSoup
import requests
import lxml
from urllib.parse import quote,unquote
import pandas as pd
from datetime import date,datetime
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
"""
抓全部氣象站 id, 名字, 縣市名稱
"""
def driver():
    url=r'https://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp'
    # open  webdriver
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(3)
    select = Select(driver.find_element_by_id('stationCounty'))
    
    search_county = driver.find_element_by_name("stationCounty")
    sleep(3)
        
    options = [x for x in search_county.find_elements_by_tag_name("option")]
    
    for element in options:
        
        county_list =list()
        
        #print (element.get_attribute("value") )
        select.select_by_value(element.get_attribute("value"))
        search_station = driver.find_element_by_name("station")
        sleep(0.5)
        station_options = [x for x in search_station.find_elements_by_tag_name("option")]
        for station in station_options:
            
            station_text = station.text
            station_id = station.get_attribute("value")
            station_list=[station_id , station_text]
            county_list.append(station_list)
        print("======================", element.get_attribute("value"))
        print(county_list)    
        df = pd.DataFrame(county_list)
        cols = ['station_id', 'station_name']
        df.to_csv(f'./config/{element.get_attribute("value")}.csv', index=None, header=cols, encoding='utf-8-sig')
        print('Saved ', element.get_attribute("value"))
            
        sleep(2)

        

    print("closed")
    driver.close()
if __name__ == "__main__":
    
    driver()
