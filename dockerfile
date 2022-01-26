FROM dc_env

ADD . /discord

WORKDIR /discord

CMD python bot.py