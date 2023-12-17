from flask import Flask
from app.blueprints import user, web
from app.extension import db


app = Flask(__name__)


# register blueprint
app.register_blueprint(user.bp)
app.register_blueprint(web.bp)


# set up database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

with app.app_context():
    db.create_all()





