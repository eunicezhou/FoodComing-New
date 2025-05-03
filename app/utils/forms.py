from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, TelField
from werkzeug.security import generate_password_hash

class LoginAuth(FlaskForm):
    account = StringField('請輸入帳號')
    password = PasswordField('請輸入密碼')
    submit = SubmitField('登入會員')
    def process_password(self):
        origin_password = self.password.data
        hashed_password = generate_password_hash(origin_password, method='scrypt')
        self.password.data = hashed_password
        return self

    def validate(self, extra_validators=None):
        is_valid = super().validate(extra_validators)
        self.process_password()
        return is_valid

class RegisterAuth(FlaskForm):
    account = StringField('請輸入帳號')
    password = PasswordField('請輸入密碼')
    email = EmailField('請輸入信箱')
    phone_num = TelField('請輸入手機號碼')
    submit = SubmitField('註冊會員')

    def process_password(self):
        origin_password = self.password.data
        hashed_password = generate_password_hash(origin_password, method='scrypt')
        self.password.data = hashed_password
        return self

    def validate(self, extra_validators=None):
        is_valid = super().validate(extra_validators)
        self.process_password()
        return is_valid