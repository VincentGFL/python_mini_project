FROM python:3.7
WORKDIR /service1
RUN sudo apt update
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["pytest", "python", "app.py"]
