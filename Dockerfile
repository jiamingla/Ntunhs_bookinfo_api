# 使用官方的 Python 執行環境作為基本的 Docker 影像
# DockerFile tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM python:3.7
 
LABEL maintainer="不該在半夜寫程式阿"
# 設定工作目錄為 /app
WORKDIR /app

# 複製目前目錄下的內容，放進 Docker 容器中的 /app
ADD . /app

 # 安裝 requirements.txt 中所列的必要套件
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir uvicorn gunicorn


COPY ./start.sh /start.sh
RUN chmod +x /start.sh
 
 
# 讓 80 連接埠可以從 Docker 容器外部存取
EXPOSE 80

# 定義環境變數
ENV NAME World

# 當 Docker 容器啟動時，自動執行 app.py
CMD ["python", "main.py"]

