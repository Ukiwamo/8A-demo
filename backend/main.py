from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session  # Session をインポート
from db import SessionLocal, init_db  # db を相対インポート
import models
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS設定
origins = [
    "http://localhost:3000",  # React開発サーバーのアドレス
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# データベースの初期化
init_db()

# データベースセッションの依存性注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ユーザ情報を取得するエンドポイント
@app.get("/user")
def read_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    logger.info(f"Fetched {len(users)} users")
    return users



@app.get("/restaurant")
def read_restaurant(db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.restaurant_id ==1 ).all()
    logger.info(f"Fetched {len(restaurant)} restaurants")
    return restaurant


@app.get("/bookmark")
def read_restaurant(db: Session = Depends(get_db)):
    bookmark = db.query(models.Bookmark).all()
    logger.info(f"Fetched {len(bookmark)} bookmarks")
    return bookmark


@app.get("/bookmark/{column_id}")
def get_bookmark(column_id: int, db: Session = Depends(get_db)):
    
    bookmark = db.query(models.Bookmark).filter(models.Bookmark.column_id == column_id).all()
    logger.info(bookmark)
    logger.info("bookmarkのカラムから取得してる")
    return bookmark

