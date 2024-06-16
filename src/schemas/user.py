from pydantic import BaseModel


class UserResponse(BaseModel):
    user_name: str
    name: str
    age: int
