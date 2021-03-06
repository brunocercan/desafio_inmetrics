from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('db_config.py')

from rotas import *

if __name__ == '__main__':
    app.run(host='0.0.0.0')