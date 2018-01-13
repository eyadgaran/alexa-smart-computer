from app import app, ask
from auth import *
from controller import *


PORT = 2080


if __name__ == '__main__':
    app.run(port=PORT)
