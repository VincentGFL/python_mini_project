FROM python:3.7
WORKDIR /service2
RUN pip install Flask
COPY app.py .
EXPOSE 5001
ENTRYPOINT ["python", "app.py"]
