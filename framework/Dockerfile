FROM python:2.7
COPY hello /opt/hello
RUN pip install -r /opt/hello/requirements.txt
WORKDIR /opt/hello
CMD python hello.py
