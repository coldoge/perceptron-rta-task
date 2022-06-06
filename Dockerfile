FROM python:3.10
WORKDIR /JanScheuring-rta
COPY requirements.txt .
COPY modules .
COPY main.py .
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]