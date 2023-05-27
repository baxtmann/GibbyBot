FROM python:latest

RUN echo "YOU MUST ENTER BOT TOKEN BEFORE RUNNING DOCKER!!"

ADD . / GibbyBot/

RUN cd GibbyBot/

RUN apt-get update

RUN apt-get install -y software-properties-common git

RUN pip3 install python-dotenv

RUN pip3 install -U git+https://github.com/Pycord-Development/pycord

RUN pip3 install openai

RUN echo "GIBBY TOKEN = ""$GIBBY_TOKEN" >> .env

CMD [ "python", "./GibbyBot/gibby.py" ]