import unittest
from flask_migrate import Migrate
import os

from app import create_app, db

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.cli.command(name="test")
def test():
    tests = unittest.TestLoader().discover("tests")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)
