FROM python:3.9.6
RUN apt update -y
WORKDIR /app 
COPY . /app 
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn app:app --bind 0.0.0.0:$PORT --worker-class aiohttp.GunicornWebWorker

