FROM python:3.6

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    -y libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["python3", "./server.py"]

#docker build -t ruby2py . && docker run -p 8000:8000 ruby2py
#docker images | grep none | awk '{print $3} ' | xargs docker rmi -f
#curl -X POST -d @input.xml  -H 'Content-Type: text/xml' http://localhost:8000