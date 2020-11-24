FROM python:3.7
WORKDIR /service1
RUN pip install flask requests
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
