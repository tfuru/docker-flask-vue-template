FROM python:3.7.3

WORKDIR /flask
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD ["chmod", "+x", "/flask/run.sh"]

# WORKDIR /flask/vue-app
# RUN apt install -y nodejs npm
# CMD ["npm", "run", "build"]
