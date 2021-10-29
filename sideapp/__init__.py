import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

(
    db_user, 
    db_pass, 
    db_name, 
    db_domain
) = (os.environ.get(item) for item in [
    "DB_USER", 
    "DB_PASS", 
    "DB_NAME", 
    "DB_DOMAIN"
    ]
)

app = Flask(__name__)

# Database address, can be used for all sql db's
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_domain}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# Hooking up flask app to database
db = SQLAlchemy(app)

class Matches(db.Model):
    __tablename__ = "matches"
    match_id = db.Column(db.Integer, primary_key = True)
    match_up = db.Column(db.String(80), unique = True, nullable = False)

    def __init__(self, match_up):
        self.match_up = match_up

    @property
    def serialize(self): 
        return {
            "match_id": self.match_id,
            "match_up": self.match_up
        }

# Creates a table from the 'db' object
db.create_all()

# App has a route
@app.route('/')
def home_page():
    return "Welcome to the Sports Tracker Homepage!"

@app.route('/signup/')
def sign_up():
    return "Users will sign up here" 

@app.route('/matchups/', methods=["GET"])
def matchups():
    matches = Matches.query.all()
    return jsonify([match.serialize for match in matches])

@app.route('/matchups/', methods=["POST"])
def create_matchup():
    new_match = Matches(request.json['match_up'])
    db.session.add(new_match)
    db.session.commit()
    return jsonify(new_match.serialize)

@app.route("/matchups/<int:id>/", methods = ["GET"])
def get_matchup(id):
    match = Matches.query.get_or_404(id)
    return jsonify(match.serialize)

@app.route("/matchups/<int:id>", methods=["PUT", "PATCH"])
def update_matchup(id):
    match = Matches.query.filter_by(match_id=id)
    match.update(dict(match_up=request.json["match_up"]))
    db.session.commit()
    return jsonify(match.first().serialize)

@app.route("/matchups/<int:id>", methods=["DELETE"])
def delete_matchup(id):
    match = Matches.query.get_or_404(id)
    db.session.delete(match)
    db.session.commit()
    return jsonfiy(match.serialize)

@app.route('/results/')
def get_results():
    return "This will be display games that have resulted"

@app.route('/result/<int:result_id>/')
def get_specific_student(result_id):
    return f"This will be a page displaying information about a specific result {result_id}"

@app.route('/news/')
def get_news():
    return "This page will display recent news articles"

@app.route('/calc/<int:f_num>/<string:operator>/<int:s_num>/')
def calc(f_num, operator, s_num):
    if operator in ["+", "-", "*"]:
        return f"{eval(f'{f_num}{operator}{s_num}')}"
    return "Please enter a valid calculation"

# Checking if this module is running 
if __name__ == '__main__':
    app.run(debug=True)

# ^^ Delivering simple website ^^
