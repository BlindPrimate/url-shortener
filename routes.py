from models.url import Url
from database import db


from flask_restful import Resource, request
from hasher import generate_hash_id


class Shorten(Resource):
    def post(self):
        url = request.args['url']
        url_model = Url(url=url)
        db.session.add(url_model)
        db.session.commit()
        return {"short_url": url}




