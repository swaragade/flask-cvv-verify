FROM python:3.6

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    -y libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

#WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["python3", "./server.py"]

#docker build -t ruby2py . && docker run -p 8000:8000 ruby2py
