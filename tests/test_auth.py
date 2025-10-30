from flask import url_for
from werkzeug.security import generate_password_hash

from app.models.models import Member
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
    
    def check_member_in_db(self, email: str):
        member = Member.check_exist(email=email)
        return member is not None
    
    # test auth_register function
    def test_auth_register(self):
        register_data  = {
            "account": "test_register",
            "password": "test_register",
            "email": "test_register@gmail.com",
            "phone_num": "0977777777",
            "submit": "true"
        }
        response = self.client.post(url_for("auth.auth_register"), 
                        data=register_data
                        )
        assert response.status_code == 200
        self.assertTrue(self.check_member_in_db(email="test_register@gmail.com"))
    
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