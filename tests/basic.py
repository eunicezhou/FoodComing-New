from unittest import TestCase

from app import create_app, db


class TestBase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()


        # Creates a test client for this application.
        self.client = self.app.test_client()
    def tearDown(self):
        self.app_context.pop()
    
    def clear_table(self, model):
        db.session.query(model).delete()
        db.session.commit()

