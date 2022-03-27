import flask

from flask_restful import Api
from flask_migrate import Migrate

from routes import Shorten
from routes import Retrieve
from database import db

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

api = Api(app)
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)

api.add_resource(Shorten, '/shorten')
api.add_resource(Retrieve, '/<string:hash_code>')


if __name__ == "__main__":
    app.run(debug=True)


