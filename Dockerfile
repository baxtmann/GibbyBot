FROM ubuntu:bionic

RUN echo "YOU MUST ENTER BOT TOKEN BEFORE RUNNING DOCKER!!"

ADD . / GibbyBot/

RUN cd GibbyBot/

RUN apt-get update

RUN apt-get install -y software-properties-common python3.8 git

RUN add-apt-repository ppa:deadsnakes/ppa

RUN update-alternatives --install /usr/bin/python3.8 python /usr/bin/python3 1

RUN apt-get install -y python3-pip

RUN pip3 install python-dotenv

RUN pip3 install -U git+https://github.com/Pycord-Development/pycord

RUN echo "GIBBY TOKEN = ""$GIBBY_TOKEN" >> .env

CMD [ "python", "./GibbyBot/gibby.py" ]