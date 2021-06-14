# Fastiapi + Fastapi + Selenium + Chromedriver in Docker on Heroku
### 之前想把fastapi部署上去heroku時怎麼樣都有問題，
    後來想想Fastapi和Flask不同之處在於它有個特性是只需要一行程式碼就可以方便的dockerize，  
    但實際上我就卡在Dockerfile裡好幾個小時才明白一些眉角，一般的程式要部署上去heroku就用Procfile，用上Docker就用Dockerfile，原來自己用是一回事，部署上去也是一回事QQ。 

#### 用docker以後
## Deploying dockerized fastAPI to Heroku  
 git clone https://github.com/askblaker/fastapi-docker-heroku.git

### 看了哪幾篇文章來解決問題
    問題：Error R10 (Boot timeout)
    “Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch” on node.js deploy with Docker in Heroku
    https://stackoverflow.com/questions/52958110/error-r10-boot-timeout-web-process-failed-to-bind-to-port-within-60-secon
    解法：要用　$port來讓docker開放heroku自動分配的Port
    問題：沒法import 其他.py檔
    Python Flask Heroku Cannot import module
    https://stackoverflow.com/questions/46250019/python-flask-heroku-cannot-import-module
    解法：
    You have to import the class using:
    from .class1 import G
    Do not forget the dot. When you build a package you have to tell where your class is written using this relative path. This is called intra-package references.

