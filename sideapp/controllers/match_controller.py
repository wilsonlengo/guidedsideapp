from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from main import db
from models.matches import Matches
from schemas.match_schema import matches_schema, match_schema

matches = Blueprint('matches', __name__)

@matches.route('/')
def home_page():
    data = {
        "page_title": "Homepage"
    }
    return render_template("homepage.html", page_data=data)

@matches.route('/signup/')
def sign_up():
    return "Users will sign up here" 

@matches.route('/matchups/', methods=["GET"])
def matchups():
    data = {
        "page_title": "Matches",
        "matches": matches_schema.dump(Matches.query.all())
    }
    return render_template("matches.html", page_data=data)

@matches.route('/matchups/', methods=["POST"])
def create_matchup():
    new_match = match_schema.load(request.form)
    db.session.add(new_match)
    db.session.commit()
    return redirect(url_for("matches.matchups"))

@matches.route("/matchups/<int:id>/", methods = ["GET"])
def get_matchup(id):
    match = Matches.query.get_or_404(id)
    data = {
        "page_title": "Matchup Detail",
        "match": match_schema.dump(match)
    }
    return render_template("matchup_detail.html", page_data=data)

@matches.route("/matchups/<int:id>/", methods=["POST"])
def update_matchup(id):
    match = Matches.query.filter_by(match_id=id)

    updated_fields = match_schema.dump(request.form)
    if updated_fields:
        match.update(updated_fields)
    #match.update(dict(match_up=request.json["match_up"]))
        db.session.commit()
    data = {
        "page_title": "Matchup Detail",
        "match": match_schema.dump(match.first())
    }
    return render_template("matchup_detail.html", page_data=data)

@matches.route("/matchups/<int:id>/delete/", methods=["POST"])
def delete_matchup(id):
    match = Matches.query.get_or_404(id)
    db.session.delete(match)
    db.session.commit()
    return redirect(url_for("matches.matchups"))

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