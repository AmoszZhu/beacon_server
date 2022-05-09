FROM python:3.8.12

WORKDIR /server
ADD . /server

RUN mkdir /tmp/logs

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt