from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from marshmallow.exceptions import ValidationError
from flask_login import LoginManager


db = SQLAlchemy()
ma = Marshmallow() # Initialization
lm = LoginManager()

def create_app(): 

    # Creating the flask app object - core of app
    app = Flask(__name__)

    app.config.from_object("config.app_config")
    
    # Creates a table from the 'db' object
    db.init_app(app)
    ma.init_app(app) # Link up
    lm.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)    

    # Registering our routes
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    @app.errorhandler(ValidationError)
    def handle_bad_reqeust(error):
        return (jsonify(error.messages), 400)

    return app

    # ^^ Delivering simple website ^^
