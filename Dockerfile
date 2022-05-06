FROM python:3.10

ENV FLASK_IP=127.0.0.1
ENV FLASK_PORT=5000
ENV MDB_IP=157.90.152.100
ENV MDB_PORT=3306
ENV MDB_USER=rn
ENV MDB_PW=dhge2022/vs!

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]