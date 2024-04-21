

from pydantic import BaseModel, Extra

class UserCreateRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    is_admin: bool

    class Config:
        extra = Extra.forbid

class UserLoginRequest(BaseModel):
    email: str
    password: str
    remember_me: bool

    class Config:
        extra = Extra.forbid

class AddTodoRequest(BaseModel):
    todo_title: str
    todo_description: str
    priority_id: int

    class Config:
        extra = Extra.forbid

class UpdateTodoRequest(BaseModel):
    id : int
    todo_title : str
    todo_description : str
    priority_id : int
    is_completed : bool

    class Config:
        extra = Extra.forbid

class AddPriorityRequest(BaseModel):
    priority: str
    class Config:
        extra = Extra.forbid