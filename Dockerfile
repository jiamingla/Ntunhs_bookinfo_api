
# DockerFile tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM python:3.7
 
LABEL maintainer="不該在半夜寫程式阿"
 
RUN pip install --no-cache-dir uvicorn gunicorn
 # 安裝 requirements.txt 中所列的必要套件
RUN pip install -r requirements.txt

COPY ./start.sh /start.sh
RUN chmod +x /start.sh
 
COPY ./gunicorn_conf.py /gunicorn_conf.py
 
COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh
 
COPY ./app /app
WORKDIR /app/
 
ENV PYTHONPATH=/app
 
EXPOSE 80
# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]


