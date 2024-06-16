# database.py
from sqlalchemy import create_engine, MetaData
from databases import Database

user = 'root'
password = 'Iwassy15'
hostname = 'localhost'
port = 3306
database = '8Apra'

# 接続URLを作成します
DATABASE_URL = f'mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}'



database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)