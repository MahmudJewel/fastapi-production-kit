# fastapi 
from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from datetime import timedelta

# # auth google 
# from starlette.requests import Request
# from starlette.responses import JSONResponse
# from fastapi.responses import RedirectResponse
# from authlib.integrations.starlette_client import OAuth

# sqlalchemy
from sqlalchemy.orm import Session

# import
from app.schemas.user import User, UserLogin, Token
from app.core.dependencies import get_db
from app.core.settings import (
    ACCESS_TOKEN_EXPIRE_MINUTES, 
    REFRESH_TOKEN_EXPIRE_DAYS,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    REDIRECT_URI,
    )
from app.api.endpoints.user import functions as user_functions


auth_module = APIRouter()

# # google ========================
# oauth = OAuth()
# oauth.register(
#     name='google',
#     client_id=GOOGLE_CLIENT_ID,
#     client_secret=GOOGLE_CLIENT_SECRET,
#     authorize_url='https://accounts.google.com/o/oauth2/auth',
#     authorize_params=None,
#     access_token_url='https://accounts.google.com/o/oauth2/token',
#     access_token_params=None,
#     refresh_token_url=None,
#     redirect_uri='http://127.0.0.1:8000/auth/google/callback',
#     client_kwargs={'scope': 'openid profile email'},
# )

# ============> login/logout < ======================
# getting access token for login 
@auth_module.post("/login", response_model= Token)
async def login_for_access_token(
    user: UserLogin,
    db: Session = Depends(get_db)
) -> Token:
    member = user_functions.authenticate_user(db, user=user)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user_functions.create_access_token(
        data={"id": member.id, "email": member.email, "role": member.role}, expires_delta=access_token_expires
    )
    
    refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    refresh_token = await user_functions.create_refresh_token(
        data={"id": member.id, "email": member.email, "role": member.role}, 
        expires_delta=refresh_token_expires
    )
    return Token(access_token=access_token, refresh_token=refresh_token, token_type="bearer")

@auth_module.post("/refresh", response_model=Token)
async def refresh_access_token(refresh_token: str, db: Session = Depends(get_db)):
    token = await user_functions.refresh_access_token(db, refresh_token)
    return token

# get curren user 
@auth_module.get('/users/me/', response_model= User)
async def read_current_user( current_user: Annotated[User, Depends(user_functions.get_current_user)]):
    return current_user


# # ============================> signin using google <========================
# @auth_module.get('/google/login')
# async def login(request: Request):
#     redirect_uri = request.url_for('auth_callback')
#     return await oauth.google.authorize_redirect(request, redirect_uri)

# @auth_module.route('/auth/google/callback') # path will be same as redirect url
# async def auth_callback(request: Request):
#     token = await oauth.google.authorize_access_token(request)
#     user = await oauth.google.parse_id_token(request, token)
#     return JSONResponse(user)

# # @auth_module.get('/protected')
# # async def protected(user: dict = Depends(oauth.google.authorize_user)):
# #     return {'message': 'This is a protected route', 'user': user}



