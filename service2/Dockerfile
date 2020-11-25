FROM python:3.7
WORKDIR /service2
RUN pip install flask requests
COPY . .
EXPOSE 5001
ENTRYPOINT ["python", "app.py"]
