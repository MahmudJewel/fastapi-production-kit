from fastapi import FastAPI


SECRET_KEY = "09027e5d4c40783326cef1ee95c179c7dcaa4c92e90844c1c1958b027546d240"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

@app.get('/')
async def read_home_page():
    return {"msg": "Initialization done"}

