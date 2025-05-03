from flask import Blueprint, redirect, url_for

from app import db
from app.models.models import Member
from app.utils.forms import RegisterAuth, LoginAuth

auth = Blueprint("auth", __name__)

@auth.post('/login')
def auth_login():

    form = LoginAuth()
    if not form.validate_on_submit():
        return redirect('/')
    
    data = form.data
    account=data.get('account')
    password=data.get('password')

    existed = Member.check_exist(account=account, password=password)
    if existed:
        return redirect('/')

    
    return redirect('/')

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

    existed = Member.check_exist(email=email)
    if existed:
        return redirect('/')
    
    Member.create_member(
        account=account,
        password=password,
        email=email,
        phone=phone 
    )
    db.session.commit()

    return redirect('/')
    

        
