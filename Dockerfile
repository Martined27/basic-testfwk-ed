FROM python:3.11.4

WORKDIR /opt/restapi_testfwk-ed
COPY requirements.txt . 
RUN pip3 install -r requirements.txt
COPY . /opt/restapi_testfwk-ed
