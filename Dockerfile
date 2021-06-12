# 使用官方的 Python 執行環境作為基本的 Docker 影像
# DockerFile tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM python:3.7
 
# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

LABEL maintainer="不該在半夜寫程式阿"
# 設定工作目錄為 /app
WORKDIR /app

# 複製目前目錄下的內容，放進 Docker 容器中的 /app
ADD . /app

 # 安裝 requirements.txt 中所列的必要套件
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir uvicorn gunicorn

#Remove EXPOSE 80 3000, because it is not used by Heroku
# 讓 80 連接埠可以從 Docker 容器外部存取
#EXPOSE 8000

# 定義環境變數
ENV NAME World

#When you deploy, the app must listen on $PORT set by Heroku. 
#Your app can access this port with process.env.PORT. 
#If you'd rather pass the port in the Dockerfile cmd 
#then you can use CMD start_app_command -p $PORT
# 當 Docker 容器啟動時，自動執行 app.py
#CMD ["python", "app/main.py"]
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT

