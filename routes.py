from models.url import Url
from database import db


from flask_restful import Resource, request
from hasher import Hasher

hash_gen = Hasher(length=6)


class Retrieve(Resource):
    def get(self, hash_code):
        url_id = hash_gen.retrieve_url_id_from_hash(hash_code)
        url = Url.query.get(url_id[0])
        return {"url": url.url}


class Shorten(Resource):
    def post(self):
        new_url = Url(url=request.args['url'])
        db.session.add(new_url)
        db.session.flush()
        id_hash = hash_gen.generate_hash_id(new_url.id, 6)
        db.session.commit()
        return {"short_url": id_hash}





