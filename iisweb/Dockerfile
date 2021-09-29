FROM python:3.9.7

#MAINTANER Your Name "mannetjie@opennetworks.com"

#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
COPY ./templates/index.html /app/templates
COPY ./static/iss4.png /app/static

ENTRYPOINT [ "python" ]

CMD [ "webapp.py" ]