FROM python:3

RUN echo "YOU MUST ENTER BOT TOEKN BEFORE RUNNING DOCKER!!"

ADD . / GibbyBot/

RUN cd GibbyBot/

RUN pip3 install -r GibbyBot/requirements.txt

CMD [ "python", "./GibbyBot/start.py" ]
