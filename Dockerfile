FROM python:3

ADD worker.py tasks.py /

RUN pip install redis rq

CMD ["python", "./worker.py"]