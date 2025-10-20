from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound

from app.utils.forms import RegisterAuth, LoginAuth
from config import config

bootstrap = Bootstrap5()
db = SQLAlchemy()
migrate = Migrate()

# Error Handler Function
def internal_server_error(e):
    pass

def not_found_error(e):
    pass

def create_app(config_name):
    app = Flask(__name__)

    # TODO: 建立 gunicorn logger 以蒐集系統錯誤問題

    # 載入 config 設定
    app.config.from_object(config[config_name])

    # 初始化套件
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # 註冊 blueprints
    @app.get('/')
    def index():
        login_form = LoginAuth()
        register_form = RegisterAuth()
 
        return render_template("index.html", 
                               register_form=register_form,
                               login_form=login_form)

    from app.routes.store.stores import store as store
    app.register_blueprint(store)
    from app.routes.auth.auth import auth as auth
    app.register_blueprint(auth)

    # 處理錯誤
    app.register_error_handler(Exception, internal_server_error)
    app.register_error_handler(NotFound, not_found_error)

    return app