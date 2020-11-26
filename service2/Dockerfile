FROM python:3.7
WORKDIR /service2
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
ENTRYPOINT ["python", "app.py"]
