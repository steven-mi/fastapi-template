from typing import Any
from fastapi import Depends, FastAPI, Request


async def this_app(request: Request) -> FastAPI:
    return request.app


async def get_from_state(app: FastAPI = Depends(this_app)) -> Any:
    app.state
    pass
