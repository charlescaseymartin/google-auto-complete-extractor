FROM --platform=linux/amd64 python:3.10-alpine
WORKDIR /scraper
COPY ./main.py ./requirements.txt .
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python", "./main.py"]
