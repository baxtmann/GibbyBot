FROM python:3

RUN echo "YOU MUST ENTER BOT TOKEN BEFORE RUNNING DOCKER!!"

ADD . / GibbyBot/

RUN cd GibbyBot/

RUN pip3 install python-dotenv

RUN pip3 install -U git+https://github.com/Pycord-Development/pycord

RUN echo "GIBBY TOKEN = ""$GIBBY_TOKEN" >> .env

CMD [ "python", "./GibbyBot/gibby.py" ]
