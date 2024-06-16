from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session  # Session をインポート
from db import SessionLocal, init_db  # db を相対インポート
import models

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
    return users



@app.get("/restaurant")
def read_restaurant(db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.restaurant_id ==1 ).all()
    return restaurant



# その他のエンドポイントや関数はここに追加する
