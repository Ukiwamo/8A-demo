from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pydantic import BaseModel

from typing import Optional


app = FastAPI()

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

@app.get("/")
def read_root():
    return {"message": "this sentence is from main.py"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# # ユーザー情報を取得するエンドポイント
# @app.get("/tasks/")
# async def read_tasks():
#     tasks = []
#     # データベースからタスク情報を取得
#     with conn:
#         cursor = conn.execute("SELECT * FROM task")
#         for row in cursor.fetchall():
#             tasks.append(dict(row))
#     return tasks


# @app.get("/practice/{content}")
# async def pra(content):
#     return {"reply": content}

# @app.get("/practice2/")
# async def pra2(content: str, detail: str):
#     return {
#         "content": content,
#         "detail": detail
#     }




# @app.post("/item/")
# async def create_item(item: Item):
#     return item