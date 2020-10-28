FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        cmake \
        build-essential \
        gcc \
        g++ 
RUN pip install -r requirements.txt
RUN python db_starter.py
#CMD python ./app.py

# Run the image as a non-root user
#RUN adduser -D myuser
#USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
#CMD gunicorn --bind 0.0.0.0:80 wsgi

#Running local:
##First, docker build . -t ytubev2
##Then, docker run -e PORT=80 -p 80:80 ytubev2


#https://github.com/microsoft/LightGBM/blob/master/docker/dockerfile-python
#https://github.com/heroku/alpinehelloworld
#https://devcenter.heroku.com/articles/container-registry-and-runtime
