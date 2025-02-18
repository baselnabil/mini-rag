from fastapi import FastAPI
from routes.base import base_router
import sys
import os


app  = FastAPI()

app.include_router(base_router)
