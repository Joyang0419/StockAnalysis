import os
from dotenv import load_dotenv
from app import create_app

# 抓取env檔案位置。
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

# 若env檔案位置存在，讀取環境變數。
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# 建立Flask的Current App
app = create_app(os.getenv('FLASK_CONFIG') or 'default')