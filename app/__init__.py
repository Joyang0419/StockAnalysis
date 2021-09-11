from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
# 匯入config.py
from configs.config import config


# 工具(尚未初始化)
db = SQLAlchemy()


def create_app(config_name):
    """flask factory"""
    app = Flask(__name__)
    # 將config.py內定義的組態類別，其所儲存的組態設定直接匯入App
    app.config.from_object(config[config_name])
    # App初始化工具，使用init_app()
    config[config_name].init_app(app)
    db.init_app(app)

    @app.route('/')
    def index():
        current_app.logger.info("123")
        return '<html><body>123</body></html>'

    return app
