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
from api.herbs import *

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
    click.echo('Inserting herbs data')
    HerbList.import_data()

@app.errorhandler(Exception)
def internal_error(err):
    """
    Global Route to handle All Error Status Codes
    """
    if isinstance(err, HTTPException):
        if type(err).__name__ == 'NotFound':
            err.description = "Not found"
        message = err.description
        code = err.code
    else:
        message = err
        code = 500

    response = {
        'status': 'failed',
        'status_code': int(code),
        'data': {
            'error': message
        },
    }
    return make_response(jsonify(response), code)

@app.errorhandler(400)
def handle_404(exception):
    """
    handles 400 errros, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    
    response = {
        'status': 'failed',
        'status_code': int(code),
        'data': {
            'error': message
        },
    }
    return make_response(jsonify(message), code)

@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 errors, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    response = {
        'status': 'failed',
        'status_code': int(code),
        'data': {
            'error': description
        },
    }
    return make_response(jsonify(response), code)