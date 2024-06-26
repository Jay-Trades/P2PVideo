from fastapi import FastAPI, Response, HTTPException
from login import router as login_router

app = FastAPI()

app.include_router(login_router, prefix='/auth')

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

