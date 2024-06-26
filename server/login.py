from fastapi import APIRouter, Depends, HTTPException, status
import sqlite3

conn = sqlite3.connect('login.db')
cursor = conn.cursor()


router = APIRouter()

@router.post("/registration")
def login(email: str, username: str, password: str):
    # Implement your login logic here
    if username == "test" and password == "password":
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        print(rows)
        return {"message": "Login successful"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@router.post("/login")
def login(username: str, password: str):
    # Implement your login logic here
    if username == "test" and password == "password":
        return {"message": "Login successful"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
