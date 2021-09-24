from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# 匯入config.py
from configs.config import config


# 工具(尚未初始化)
db = SQLAlchemy()
# 資料庫遷移腳本
migrate = Migrate()


def create_app(config_name):
    """flask factory"""
    app = Flask(__name__)
    # 將config.py內定義的組態類別，其所儲存的組態設定直接匯入App
    app.config.from_object(config[config_name])
    # App初始化工具，使用init_app()
    config[config_name].init_app(app)
    # 實體化工具
    db.init_app(app)
    migrate.init_app(app, db)
    # 匯入model
    from app.models import (
        stock_basic_info,
        daily_price_info
    )
    # 匯入blueprint
    # command
    from app.commands.test import test as test_blueprint
    app.register_blueprint(test_blueprint)

    @app.route('/')
    def index():
        current_app.logger.info("123")
        print(current_app.config["SQLALCHEMY_DATABASE_URI"])
        return '<html><body>123</body></html>'

    return app
