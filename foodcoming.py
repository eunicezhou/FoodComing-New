from flask_migrate import Migrate
import os

from app import create_app, db
from config import config
from app.models.models import Store, Menu, Member


app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)