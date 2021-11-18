# Serializes matches
from main import ma
from models.matches import Matches
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length

class MatchSchema(ma.SQLAlchemyAutoSchema):
    match_id = auto_field(dump_only=True)
    match_up = auto_field(required=True, validate=Length(min=1)) # Atleast 1 character required for match_up
    description = auto_field(validate=Length(min=1))

    class Meta:
        model = Matches
        load_instance = True
    

match_schema = MatchSchema()
matches_schema = MatchSchema(many=True)