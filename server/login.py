from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from sqlite3 import Connection
from typing import Generator
import uuid
import bcrypt



router = APIRouter()

# def get_db_conn() -> Generator:
#     with get_db() as db:
#         yield db
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return str(hashed_password)

@router.post("/registration")
def registration(email: str, username: str, password: str, db: Connection = Depends(get_db)):
    #depends just calls a callable before going into the function. In this case setting db connection to db. It is auto injected
    
    # Implement your login logic here
    cursor = db.cursor()
    #check if email is alreaady in the db if it is return false message
    cursor.execute('SELECT email FROM User WHERE email == ?',(email,))
    email_exists = cursor.fetchone()

    if email_exists is not None:
        print(email_exists)
        print('There exists an email', email_exists is not None)
        return {"message": "User already exists"}
    #if not false update the db with the email username and add password into the password table with the same UUID
    main_table_id = str(uuid.uuid4())
    hashed_password = hash_password(password)
    print((main_table_id))
    print((email))
    print((username))

    cursor.execute('INSERT INTO User (ID, email, username) VALUES (?,?,?)', (main_table_id, email, username))
    cursor.execute('INSERT INTO Password (ID, password_hash) VALUES (?,?)', (main_table_id, hashed_password))
    db.commit()
    return {"message": "Registration successful"}

    # if username == "test" and password == "password":
    #     return {"message": "Login successful"}
    # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@router.post("/login")
def login(username: str, password: str):
    # Implement your login logic here
    if username == "test" and password == "password":
        return {"message": "Login successful"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
