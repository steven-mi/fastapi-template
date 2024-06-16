from fastapi.testclient import TestClient
from httpx import AsyncClient
import pytest_asyncio
from asyncio import get_event_loop
from src.main import app


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
def anyio_backend():
    return "asyncio"


@pytest_asyncio.fixture(scope="module")
async def client():
    with TestClient(app):  # This will trigger the lifespan events
        async with AsyncClient(app=app, base_url="http://test") as c:
            yield c
