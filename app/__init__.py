from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def run_app():
    app = Flask(__name__)