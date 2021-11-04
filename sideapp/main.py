from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 


db = SQLAlchemy()
ma = Marshmallow() # Initialization

def create_app(): 

    app = Flask(__name__)

    app.config.from_object("config.app_config")
    
    # Creates a table from the 'db' object
    db.init_app(app)
    ma.init_app(app) # Link up

   
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)


    return app

    # ^^ Delivering simple website ^^
