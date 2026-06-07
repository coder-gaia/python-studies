from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    title: str


class TaskResponse(BaseModel):
    id: str
    title: str
    completed: bool
    user_id: str

    class Config:
        from_attributes = True