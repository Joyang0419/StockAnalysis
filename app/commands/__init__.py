from flask import Blueprint

test = Blueprint('test', __name__)
test.cli.short_help = '測試功能'
