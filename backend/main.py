from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session  # Session をインポート
from db import SessionLocal, init_db  # db を相対インポート
from models import User  # models を相対インポート

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
    users = db.query(User).all()
    return users

# その他のエンドポイントや関数はここに追加する
