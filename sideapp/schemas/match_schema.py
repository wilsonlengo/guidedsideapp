# Serializes matches
from main import ma
from models.matches import Matches
from marshmallow_sqlalchemy import auto_field

class MatchSchema(ma.SQLAlchemyAutoSchema):
    match_id = auto_field(dump_only=True)

    class Meta:
        model = Matches
        load_instance = True
    

match_schema = MatchSchema()
matches_schema = MatchSchema(many=True)