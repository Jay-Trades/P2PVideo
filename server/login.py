from fastapi import APIRouter, Depends, HTTPException, status, Security, Request
from fastapi.responses import JSONResponse
from database import get_db
from sqlite3 import Connection
from typing import Generator
import uuid
import bcrypt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer




#test users
#jay@gmail.com pw:test2 username:test1
#bboynamu@gmail.com pw:bboykoreice0 username:lethalasian 
#jayleonchen@gmail.com  pw:13579j username:koreice0ß


router = APIRouter()
access_security = JwtAccessBearer(secret_key="jfdlsajflskajdfklaaaa", auto_error=True)
#auto_error: If set to True, an HTTPException will be automatically raised if the token is invalid or missing.
# breakpoint()


# def get_db_conn() -> Generator:
#     with get_db() as db:
#         yield db

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


    
@router.post("/registration")
def registration(email: str, username: str, password: str, db: Connection = Depends(get_db)):
    #depends just calls a callable before going into the function. In this case setting db connection to db. It is auto injected
    
    cursor = db.cursor()
    #check if email is alreaady in the db if it is return false message
    cursor.execute('SELECT email, username FROM User WHERE email == ?',(email,))
    email_exists = cursor.fetchone()
    if email_exists is not None:
        print(email_exists)
        print('There exists an email', email_exists is not None)
        return {"message": "User already exists"}
    
    cursor.execute('SELECT username FROM User WHERE username == ?',(username,))
    user_exists = cursor.fetchone()

    if user_exists is not None:
        print('user-name exists')
        return {"message": "Username is taken please use a different one"}
    
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
def login(email: str, username: str, password: str, db: Connection = Depends(get_db)):
    cursor = db.cursor()
    #check if email is in the DB if not return error message
    cursor.execute('SELECT * FROM User WHERE email == ?',(email,))
    data = cursor.fetchone()
    if data is None:
        return {"message": "Login failed, email not registered"}
    
    uuid, _, _ = data    

    cursor.execute('SELECT * FROM Password WHERE ID == ?',(uuid,))
    pw_data = cursor.fetchone()
    _, pw_hash = pw_data
    print(_, pw_hash)

    is_valid = verify_password(password, pw_hash) #verify password hash is a match

    if is_valid:
        #logged in logic
        subject = {"username": username, "role": "user"}
        return {"access_token": access_security.create_access_token(subject=subject)}
        # return {"message": "We good"}

    else:
        return {"message": "Login failed, email password combination does not match"}

@router.get("/protected-route")
def protected_route(credentials: JwtAuthorizationCredentials = Security(access_security)):
    #you can turn an obj into a dict to see whats inside it with __dict__
    credentials_dict = credentials.__dict__ 
    print(credentials_dict)
    return {"message": f"Hello, {credentials.subject['username']}!"}