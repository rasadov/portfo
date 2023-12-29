from flask import Flask
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = 'fPfKdLHcBn7JOCeDxPORUns0ZSo9i4HY'

from main import routes