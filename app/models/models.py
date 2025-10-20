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

    @classmethod
    def check_exist(cls, **kwargs):

        exist = cls.query

        if kwargs.get("email"):
            exist = exist.filter(cls.email == kwargs["email"])

        return exist.first()

    @classmethod
    def create_member(cls, commit: bool=False, **kwargs):
        
        new_member = cls(**kwargs)
        db.session.add(new_member)

        if commit:
            db.session.commit()
        
        return new_member

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