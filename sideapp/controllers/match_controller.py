from flask import Blueprint, jsonify, request
from main import db
from models.matches import Matches
from schemas.match_schema import matches_schema, match_schema

matches = Blueprint('matches', __name__)

@matches.route('/')
def home_page():
    return "Welcome to the Sports Tracker Homepage!"

@matches.route('/signup/')
def sign_up():
    return "Users will sign up here" 

@matches.route('/matchups/', methods=["GET"])
def matchups():
    matches = Matches.query.all()
    return jsonify(matches_scehma.dump(matches))

@matches.route('/matchups/', methods=["POST"])
def create_matchup():
    new_match = match_schema.load(request.json)
    db.session.add(new_match)
    db.session.commit()
    return jsonify(match_schema.dump(new_match))

@matches.route("/matchups/<int:id>/", methods = ["GET"])
def get_matchup(id):
    match = Matches.query.get_or_404(id)
    return jsonify(match_schema.dump(new_match))

@matches.route("/matchups/<int:id>", methods=["PUT", "PATCH"])
def update_matchup(id):
    match = Matches.query.filter_by(match_id=id)
    updated_fields = match_schema.dump(request.json)
    if updated_fields:
        match.update(updated_fields)
    #match.update(dict(match_up=request.json["match_up"]))
        db.session.commit()
    return jsonify(match_schema.dump(match.first()))

@matches.route("/matchups/<int:id>", methods=["DELETE"])
def delete_matchup(id):
    match = Matches.query.get_or_404(id)
    db.session.delete(match)
    db.session.commit()
    return jsonfiy(match.schema.dump(match))

@matches.route('/results/')
def get_results():
    return "This will be display games that have resulted"

@matches.route('/result/<int:result_id>/')
def get_specific_student(result_id):
    return f"This will be a page displaying information about a specific result {result_id}"

@matches.route('/news/')
def get_news():
    return "This page will display recent news articles"

@matches.route('/calc/<int:f_num>/<string:operator>/<int:s_num>/')
def calc(f_num, operator, s_num):
    if operator in ["+", "-", "*"]:
        return f"{eval(f'{f_num}{operator}{s_num}')}"
    return "Please enter a valid calculation"