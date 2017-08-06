from flask import Flask
from flask_ask import Ask
import logging

app = Flask(__name__)
ask = Ask(app, "/")


# TODO: figure out logging handlers
FORMAT = "[%(asctime)s %(name)s] %(message)s"
# logging.basicConfig(format=FORMAT)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.DEBUG)
