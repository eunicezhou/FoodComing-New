from flask import json, url_for
from werkzeug.security import generate_password_hash

from app.models.models import Member
from app import db
from tests.basic import TestBase


class TestAuth(TestBase):
    def setUp(self):
        super().setUp()
        self.member = self.create_member()

    def tearDown(self):
        self.clear_table(Member)
        super().tearDown()
        
    def create_member(self):
        hashed_password = generate_password_hash("test_login")
        new_member = Member.create_member(
                        commit=True,
                        account="test_login",
                        password=hashed_password,
                        email="test_login@gmail.com",
                        phone="0988888888"
                    )
        return new_member
    
    # test auth_login function
    def test_auth_login(self):
        auth_data  = {
            "email": "test_login@gmail.com",
            "password": "test_login",
            "submit": "true"
        }
        response = self.client.post(url_for("auth.auth_login"), 
                        data=auth_data
                        )
        assert response.status_code == 200