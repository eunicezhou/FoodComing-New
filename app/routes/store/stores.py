from flask import Blueprint
from app import db
from app.models.models import Menu, Store

store = Blueprint("store", __name__)

@store.get("/<int:id>")
def get_store_info(id: int):
    store_menu_info = db.query(Store, Menu).join(Menu)\
        .filter(Store.id == id)
    