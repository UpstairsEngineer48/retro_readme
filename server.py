from fastapi import FastAPI
from src.api import router

app = FastAPI(
    title="Retro README",
)

app.include_router(router)