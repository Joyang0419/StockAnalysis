from app import db
from . import ModelAbstract


class StockBasicInfo(ModelAbstract):
    id = db.Column(db.Integer, primary_key=True)
    stock_code = db.Column(db.String(10), unique=True, nullable=False)
    stock_name = db.Column(db.String(40), unique=True, nullable=False)
    # relationship
    # stock_basic_info : daily_price_info = one to many
    daily_price_info = db.relationship('DailyPriceInfo', backref='stock_basic_info', lazy=True)


