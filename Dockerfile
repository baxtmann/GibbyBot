FROM ubuntu:bionic

RUN echo "YOU MUST ENTER BOT TOKEN BEFORE RUNNING DOCKER!!"

ADD . / GibbyBot/

RUN cd GibbyBot/

RUN apt-get update

RUN apt-get install -y software-properties-common python3.8 git

RUN add-apt-repository ppa:deadsnakes/ppa

RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6

RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8

RUN update-alternatives  --set python /usr/bin/python3.8

RUN apt-get install -y python3-pip

RUN pip3 install python-dotenv

RUN pip3 install -U git+https://github.com/Pycord-Development/pycord

RUN echo "GIBBY TOKEN = ""$GIBBY_TOKEN" >> .env

CMD [ "python", "./GibbyBot/gibby.py" ]