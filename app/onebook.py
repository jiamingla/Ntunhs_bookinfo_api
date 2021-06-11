# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options

import unittest, time, re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import math
import json
import sys
import os

#Link_to_page_URL = sys.argv[1:] #直接在run .py時加入"網址"就可以使用了

#if (Link_to_page_URL == ""):
#    print("未輸入網址")
#類別 Class
#什麼時候該用類別？
# 有此一說，當將某些狀態與功能黏在一起時，適合用類別。

#突然發現onebook這整個功能好像不需要selenium，但是複雜一點就需要用到了，
#而且也需要面對各種例外狀況，不過soup可能還是做得到
class NTUNHSLibCrawler(object):
    def __init__(self,book_url):
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        #https://aishuafei.com/heroku-selenium/
        #有教學
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument('log-level=2') #減少不必要的警告訊息
        
        #----------#
        #self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        #沒加版本號不知道能不能過
        self.driver = webdriver.Chrome()
        #----------#
        self.driver.implicitly_wait(30)#先等等
        self.base_url = "https://www.google.com/"#起始URL
        self.verificationErrors = []
        self.accept_next_alert = True
        #我還不懂這兩行能幹嘛
        self.book = []
        """
        這邊放整個爬蟲流程，去呼叫下面的函數
        """
        #爬資料
        self.book_url = book_url
        self.parse_bookinfo(self.book_url)
        #存進去資料庫
        #
    def parse_bookinfo(self,Link_to_page_URL):
        #Keywword = 'python'
        #filename = Keyword +'.json'
        driver = self.driver
        driver.get(Link_to_page_URL)
        
        html = driver.page_source
        #得到當前發好session的網址
        soup = BeautifulSoup(html, features='html.parser')
        #丟到解析庫

        #只有一本書的時候
        bookdata = soup.find('ul', {"class": 'tab_panels pct70 detail_page'})
        list = [s for s in bookdata.stripped_strings]
        image_url =  str(soup.select("body > div.columns_container > div.column.pct75.details_left_column > form:nth-child(1) > div.content_container.item_details > div.content > ul.itemservices > li:nth-child(7) > a > img "))[24:79] +"e"
        
        driver.implicitly_wait(1)
        try:
            driver.find_element_by_link_text("預約")
            print("可預約")
            driver.implicitly_wait(0)
        except NoSuchElementException as e:
            print("無預約")
        bookinfo = list[1:13]
        bookstatus = list[19:28]
        book = bookinfo + bookstatus
        book.append(image_url)
        print(bookinfo)
        print(bookstatus)
        self.driver.close()#關閉瀏覽器
        self.book = book
        return True
    
            
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    c = NTUNHSLibCrawler(book_url='http://140.131.94.8/uhtbin/cgisirsi/x/0/0/57/5/3?searchdata1=358610\{CKEY\}&searchfield1=GENERAL^SUBJECT^GENERAL^^&user_id=WEBSERVER')