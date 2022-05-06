FROM python:3.10

ENV REST_IP=127.0.0.1
ENV REST_PORT=5000
ENV DB_IP=157.90.152.100
ENV DB_PORT=3306

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]