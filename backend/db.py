from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, Bookmark, Restaurant  # models を相対インポート

# データベースの接続情報
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Iwassy15@localhost/8Apra"

# SQLAlchemyエンジンの作成
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# セッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 初期化関数
def init_db():
    Base.metadata.create_all(bind=engine)
