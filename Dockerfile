FROM ubuntu:bionic

RUN echo "YOU MUST ENTER BOT TOKEN BEFORE RUNNING DOCKER!!"

ADD . / GibbyBot/

RUN cd GibbyBot/

RUN apt-get update

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get install -y software-properties-common python3.8 git

RUN update-alternatives  --set python /usr/bin/python3.8

RUN apt-get install -y python3-pip

RUN pip3 install python-dotenv

RUN pip3 install -U git+https://github.com/Pycord-Development/pycord

RUN echo "GIBBY TOKEN = ""$GIBBY_TOKEN" >> .env

CMD [ "python", "./GibbyBot/gibby.py" ]