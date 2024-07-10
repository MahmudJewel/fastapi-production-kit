# fastapi 
from fastapi import APIRouter

# auth google 
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth

# import 
from app.core.settings import (
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    REDIRECT_URI,
    )

social_auth_module = APIRouter()

# google ========================
oauth = OAuth()
oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://127.0.0.1:8000/auth/google/callback',
    client_kwargs={'scope': 'openid profile email'},
)

# ============================> signin using google <========================
@social_auth_module.get('/google/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@social_auth_module.route('/auth/google/callback') # path will be same as redirect url
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)
    return JSONResponse(user)

# @auth_module.get('/protected')
# async def protected(user: dict = Depends(oauth.google.authorize_user)):
#     return {'message': 'This is a protected route', 'user': user}