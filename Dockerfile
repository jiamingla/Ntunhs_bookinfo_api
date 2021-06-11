FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

# 安裝 requirements.txt 中所列的必要套件
RUN pip install -r requirements.txt
