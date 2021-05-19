from flask import Flask, jsonify, request
from config import Config, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
from dotenv import load_dotenv
import click

load_dotenv('.env')
app = Flask(__name__)
app.config.from_object(ProductionConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.users import User
from models.favorites import Favorite
from models.herb_list import HerbList
from models.history import History
from models.premium_status import PremiumStatus
from models.roles import Role

from api.accounts import *

version = "0.1"

@app.route('/')
def index():
    ts = time.time()
    return jsonify({"version":version,"time": str(time.time()-ts)})

@app.cli.command()
def seed_data():
    """Init Default Data"""
    click.echo('Inserting roles data')
    Role.generate_default_roles()
