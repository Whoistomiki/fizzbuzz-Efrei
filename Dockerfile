FROM python:3.9-slim

WORKDIR /app

COPY fizzbuzz.py test_fizzbuzz.py /app/

RUN pip install pytest

CMD ["pytest", "test_fizzbuzz.py"]
