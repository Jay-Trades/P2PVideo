from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, Security, Request
from fastapi.responses import JSONResponse
from login import router as login_router
from authlib.jose.errors import BadSignatureError, ExpiredTokenError
# from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer



app = FastAPI()

app.include_router(login_router, prefix='/auth')

# access_security = JwtAccessBearer(secret_key="jfdlsajflskajdfklaaaa", auto_error=True)

@app.middleware("http")
async def jwt_error_handling_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except BadSignatureError:
        return JSONResponse(status_code=401, content={"detail": "Invalid token signature"})
    except ExpiredTokenError:
        return JSONResponse(status_code=401, content={"detail": "Token has expired"})
    except HTTPException as exc:
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
    except Exception as exc:
        return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
    
@app.get("/")
async def root():
    return {'message': "hello world"}

@app.get("/status")
async def get_status():
    return {'status': "OK"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=400, detail="Item ID cannot be zero")
    return {"item_id": item_id}

