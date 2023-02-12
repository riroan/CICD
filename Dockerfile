FROM python:latest

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]

EXPOSE 9000
