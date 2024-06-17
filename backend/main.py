from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session  # Session をインポート
from db import SessionLocal, init_db  # db を相対インポート
import models
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost:3000",  # Reactの開発サーバーのアドレス
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
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
    #logger.info(f"Fetched {len(users)} users")
    return users



@app.get("/restaurant")
def read_restaurant(db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.restaurant_id ==1 ).all()
   #logger.info(f"Fetched {len(restaurant)} restaurants")
    return restaurant


@app.get("/bookmark")
def read_restaurant(db: Session = Depends(get_db)):
    bookmark = db.query(models.Bookmark).all()
   # logger.info(f"Fetched {len(bookmark)} bookmarks")
    return bookmark


@app.get("/bookmark/{column_id}")
def get_bookmark(column_id: int, db: Session = Depends(get_db)):
    
    bookmark = db.query(models.Bookmark).filter(models.Bookmark.column_id == column_id).all()
    if not bookmark:
        return {"message": "Bookmark not found"}

    # restaurant_id = bookmark[0].restaurant_id
    # logger.info(restaurant_id)

        #ここから該当のレストラン情報を取得する
    restaurant_info = db.query(models.Restaurant).filter(models.Restaurant.restaurant_id == bookmark[0].restaurant_id).first()
    logger.info(f"レストラン情報は{restaurant_info.name}")


    #logger.info({bookmark, restaurant_info})
    return bookmark, restaurant_info

