from fastapi import APIRouter
from api.endpoints.user import user_router
from api.endpoints.todo import todo_router
from api.endpoints.extra import extra_router
from config.config import API_VERSION

router1 = APIRouter(prefix=API_VERSION)

router1.include_router(user_router, tags=["users"])
router1.include_router(todo_router, tags=["todos"])
router1.include_router(extra_router, tags=["extras"])
