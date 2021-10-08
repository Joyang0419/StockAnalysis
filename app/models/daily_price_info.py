import datetime

from app import db
from . import ModelAbstract


class DailyPriceInfo(ModelAbstract):
    id = db.Column(db.Integer, primary_key=True)
    stock_basic_info_id = db.Column(db.Integer, db.ForeignKey('stock_basic_info.id'), nullable=False)
    volume = db.Column(db.Integer)
    closing_price = db.Column(db.Float, nullable=False)
    opening_price = db.Column(db.Float, nullable=False)
    highest_price = db.Column(db.Float, nullable=False)
    lowest_price = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.date)

