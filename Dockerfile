FROM python:3.7-slim

RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY pipe /
COPY LICENSE.txt pipe.yml README.md /

ENTRYPOINT ["python3", "/pipe.py"]
