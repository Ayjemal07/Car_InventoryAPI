from flask import Flask, render_template
from config import Myconfig
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import db as root_db, login_manager, ma
from flask_cors import CORS
from app.helpers import JSONEncoder

app = Flask(__name__)
CORS(app)
print("Hello World")
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

print(Myconfig.__dict__)
app.json_encoder = JSONEncoder
app.config.from_object(Myconfig)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)
