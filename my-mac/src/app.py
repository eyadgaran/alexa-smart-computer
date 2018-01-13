from flask import Flask
from flask_ask import Ask
import logging
from logging.handlers import TimedRotatingFileHandler
import os


app = Flask(__name__)
ask = Ask(app, "/")

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIRECTORY = os.path.split(CURRENT_DIRECTORY)[0]
LOG_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'logs/')
logfile = LOG_DIRECTORY + 'mymac.log'


FORMAT = "[%(asctime)s %(name)s] %(message)s"
rotating_handler = TimedRotatingFileHandler(filename=logfile, when='midnight')
rotating_handler.setLevel(logging.DEBUG)
rotating_handler.setFormatter(FORMAT)


app.logger.addHandler(rotating_handler)
