Fastapi + Selenium + Chromedriver in Docker on Heroku 
====
之前想把Fastapi部署上去heroku時怎麼樣都有問題，<br>
後來想想Fastapi和Flask不同之處在於，<br>
Fastapi有個特性是只需要一行程式碼就可以方便的dockerize，<br>
但實際上我就卡在Dockerfile裡好幾個小時才明白一些眉角，<br>
一般的程式要部署上去heroku就用Procfile，用上Docker就用Dockerfile，<br>
原來自己用是一回事，部署上去也是一回事QQ。 
------

### 有使用別人寫好的Fastapi
### Deploying dockerized fastAPI to Heroku  
 git clone https://github.com/askblaker/fastapi-docker-heroku.git

### 看了哪幾篇文章來解決問題
問題：Error R10 (Boot timeout)<br>
“Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch” on node.js deploy with Docker in Heroku<br>
https://stackoverflow.com/questions/52958110/error-r10-boot-timeout-web-process-failed-to-bind-to-port-within-60-secon<br>
解法：要用　$port來讓docker開放heroku自動分配的Port<br>

問題：沒法import 其他.py檔<br>
Python Flask Heroku Cannot import module<br>
https://stackoverflow.com/questions/46250019/python-flask-heroku-cannot-import-module<br>
解法：加一個點.<br>
You have to import the class using:<br>
`from .class1 import G`<br>
Do not forget the dot. <br>When you build a package you have to tell where your class is written using this relative path. This is called intra-package references.<br>

問題：DevToolsActivePort file doesn't exist.<br>
https://ask.csdn.net/questions/6184568<br>
解法：加入幾行<br>
```py
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--no-sandbox") 
```
然後記得這句也要附上，不然會跟我一樣又多花半小時找答案<br>
```py
self.driver = webdriver.Chrome(chrome_options=chrome_options)
```
<br>
其他的參考資料或是可能用得到的東西：<br>
https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker<br>
https://github.com/heroku/heroku-buildpack-chromedriver<br>
https://blog.gtwang.org/virtualization/docker-basic-tutorial/2/<br>
https://blog.csdn.net/weixin_42493346/article/details/105854898<br>
其他問題有機會我再研究，<br>
我的期末重點不是這個API而是要CALL這個API的APP阿XD<br>