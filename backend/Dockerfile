FROM python:3.7-alpine

WORKDIR /app

# Copy app to container
COPY app/main.py /app

# install flask and mysql connector
RUN pip3 install Flask && pip3 install --upgrade pip
RUN pip3 install mysql-connector-python

# Run app
CMD [ "python3", "/app/main.py" ]