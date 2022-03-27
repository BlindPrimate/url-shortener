import flask

from flask_restful import Api
from flask_migrate import Migrate

from routes import Shorten
from database import db

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
api = Api(app)
migrate = Migrate(app=app, db=db)


api.add_resource(Shorten, '/shorten')


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)


