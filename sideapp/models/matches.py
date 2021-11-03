from main import db


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
