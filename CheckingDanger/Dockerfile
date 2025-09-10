ROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "maneger.py"]



הרצה
docker build -t myapp .
docker run -p 8000:8000 myapp