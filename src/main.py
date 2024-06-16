from fastapi import FastAPI
from src.routers import user
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    pass
    yield
    pass


app = FastAPI()


app.include_router(user.router)
