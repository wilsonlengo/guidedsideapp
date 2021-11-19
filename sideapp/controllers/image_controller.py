from flask import Blueprint, request, redirect, abort, url_for, current_app
from pathlib import Path 
from models.matches import Matches
import boto3

match_images = Blueprint('match_images', __name__)

@match_images.route("/matchups/<int:id>/image/", method=["POST"])
def update_image(id):
    
    match = Matches.query.get_or_404(id)
   
    if "image" in request.files:
       
        image = request.files["image"]
        
        if Path(image.filename).suffix != ".png":
            return abort(400, description="Invalid file type") 
        
        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        bucket.upload_fileobj(image, match.image_filename)
        
        image.save(f"static/{match.image_filename}")

        return redirect(url_for("matches.get_matchup", id=id))

    return abort(400, description="No Image")