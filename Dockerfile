FROM python:3.9.15-slim

ADD monitor.py /

ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "-u", "./monitor.py" ]
