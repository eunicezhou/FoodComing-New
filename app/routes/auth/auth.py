from datetime import datetime, timedelta
from typing import Dict, List
from flask import Blueprint, jsonify, redirect, request, current_app
from werkzeug.security import check_password_hash

from app import db
from app.models.models import Member
from app.utils.forms import RegisterAuth, LoginAuth
from app.utils.jwt import decoding, encoding

auth = Blueprint("auth", __name__)

@auth.get('/login')
def check_login():

    user_info = None
    if request.headers.get("Authorization"):
        token = request.headers.get("Authorization")
        split_token: List = token.split("Bearer ")
        target_token = split_token[1]

        token_key = current_app.config.get("SECRET_KEY")
        decoding_algorithm = current_app.config.get("ALGORITHM") 
        user_info = decoding(target_token, token_key, decoding_algorithm)

    return user_info

@auth.post('/login')
def auth_login():

    form = LoginAuth()

    if not form.validate_on_submit():
        return jsonify({"msg": "Invalid form data"}), 400
    
    data = form.data
    email=data.get('email')
    password=data.get('password')   

    existed: Member = Member.check_exist(email)

    if  not existed:
        return jsonify({"msg": "Account not exist."}), 401

    password_correct = check_password_hash(existed.password, password)
    if not password_correct:
        return jsonify({"msg": "帳號或密碼錯誤"}), 401
    
    token_key = current_app.config.get("SECRET_KEY")
    encoding_algorithm = current_app.config.get("ALGORITHM") 

    user_info = {
        "id": existed.member_id,
        "account": existed.account,
        "email": existed.email,
        "phone": existed.phone,
        "exp": datetime.utcnow() + timedelta(days=7)
    }

    encode_token: Dict = encoding(user_info=user_info, token_key=token_key, 
                            algorithm=encoding_algorithm)
    
    return jsonify(encode_token), 200
    
@auth.post('/register')
def auth_register():

    form = RegisterAuth()

    if not form.validate_on_submit():
        return redirect('/')
    
    data = form.data
    account=data.get('account')
    password=data.get('password')
    email=data.get('email')
    phone=data.get('phone_num')

    existed = Member.check_exist(email)
    if existed:
        return jsonify({"msg": "帳號已存在"}), 401
    
    Member.create_member(
        account=account,
        password=password,
        email=email,
        phone=phone 
    )
    db.session.commit()

    return jsonify({"msg": "成功註冊會員，請登入帳號"}), 200