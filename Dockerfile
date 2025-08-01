FROM python:3.11.0-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]