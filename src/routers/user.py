from typing import List
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from src.schemas.user import UserResponse

router = APIRouter(prefix="/users", tags=["user"])


@router.get("", response_class=ORJSONResponse)
async def get_users() -> List[UserResponse]:
    users = [
        UserResponse(user_name="steven", name="steven", age=20),
        UserResponse(user_name="steve", name="steve", age=17),
    ]
    return users


@router.get("/{user_name}", response_class=ORJSONResponse)
async def get_user_by_name(user_name: str) -> UserResponse:
    return UserResponse(user_name=user_name, name="steven", age=20)
