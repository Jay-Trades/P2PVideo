from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from sqlite3 import Connection
from typing import Generator



router = APIRouter()

def get_db_conn() -> Generator:
    with get_db() as db:
        yield db

@router.post("/registration")
def login(email: str, username: str, password: str, db: Connection = Depends(get_db_conn)):
    # Implement your login logic here
    cursor = db.cursor()
    cursor.execute('SELECT * FROM User')
    rows = cursor.fetchall()
    print(rows)
    if username == "test" and password == "password":
        return {"message": "Login successful"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@router.post("/login")
def login(username: str, password: str):
    # Implement your login logic here
    if username == "test" and password == "password":
        return {"message": "Login successful"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
