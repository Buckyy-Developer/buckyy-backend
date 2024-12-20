
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

# from . import models
from .database import engine

import os

# from .api import api_router
# from .core.config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Buckyy Payment Solutions",
)

origins = [
    "http://localhost:8080",
    "http://localhost:8000"
]

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(api_router)

# if not os.path.exists(settings.UPLOAD_LOCATION):
#     print(f'UPLOAD_LOCATION : "{settings.UPLOAD_LOCATION}" not found. We create it')
#     os.makedirs(settings.UPLOAD_LOCATION)

# if not os.path.exists(settings.UPLOAD_UNITYBUILD_LOCATION):
#     print(f'UPLOAD_UNITYBUILD_LOCATION : "{settings.UPLOAD_UNITYBUILD_LOCATION}" not found. We create it')
#     os.makedirs(settings.UPLOAD_UNITYBUILD_LOCATION)
