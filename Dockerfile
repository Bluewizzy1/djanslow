FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUn pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]