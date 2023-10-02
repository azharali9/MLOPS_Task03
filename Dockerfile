FROM python:3.11.5

WORKDIR /MLOPS_TASK03

COPY . /MLOPS_TASK03

RUN pip3 install flask


EXPOSE 5000

CMD ["python3", "app.py"]

