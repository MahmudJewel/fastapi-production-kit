# fastapi 
from fastapi import FastAPI, Depends, Request

# import 
from app.core.settings import config
from app.core.modules import init_routers, make_middleware



def create_app() -> FastAPI:
    app_ = FastAPI(
        title="FastAPI kit for production",
        description="FastAPI kit by Mahmud",
        version="1.0.0",
        docs_url=None if config.ENVIRONMENT == "production" else "/docs",
        redoc_url=None if config.ENVIRONMENT == "production" else "/redoc",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    # init_listeners(app_=app_)
    # init_cache()
    return app_


app = create_app()





