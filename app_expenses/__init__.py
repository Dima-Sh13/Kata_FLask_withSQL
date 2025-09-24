from flask import Flask

app = Flask(__name__)
ORIGIN_DATA="data/movimientos.sqlite"
from app_expenses.routes import *

