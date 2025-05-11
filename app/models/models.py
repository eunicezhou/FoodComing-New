from typing import Optional
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

from app import db

class Member(db.Model):
    __tablename__ = 'members'
    member_id = db.Column(db.Integer, primary_key=True, index=True)
    account = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)

    store = db.relationship("Store", back_populates="member", uselist=False)

    @staticmethod
    def check_exist(
        account: Optional[str]=None, 
        email: Optional[str]=None):

        base_query = Member.query

        if account:
            query_data = base_query.filter(Member.account == account)
        if email:
            query_data = base_query.filter(Member.email == email)

        exist = query_data.first()
        return exist

    @staticmethod
    def create_member(account: str, 
                      password: str, 
                      email: str, 
                      phone: str) -> None:
        
        new_member = Member(
            account=account,
            password=password,
            email=email,
            phone=phone
        )
        db.session.add(new_member)

class Store(db.Model):
    __tablename__ = "stores"
    store_id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    open_time = db.Column(db.Time)
    close_time = db.Column(db.Time)
    holiday = db.Column(ARRAY(db.String))
    store_photo = db.Column(db.String)

    # relationship
    # FK:
    member_id = db.Column(db.Integer, db.ForeignKey('members.member_id'))

    # 關聯回去
    member = db.relationship("Member", back_populates="store")
    menu = db.relationship("Menu", back_populates="store")

class Menu(db.Model):
    __tablename__ = "menus"
    menu_id = db.Column(db.Integer, primary_key=True, index=True)
    content = db.Column(MutableDict.as_mutable(JSONB))

    # relationship
    # FK:
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)

    store = db.relationship("Store", back_populates="menu")