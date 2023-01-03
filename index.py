
from fastapi import FastAPI
from routes.user import use

appp = FastAPI()
appp.include_router(use)

