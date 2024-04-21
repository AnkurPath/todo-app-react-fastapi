from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from core.schemas import AddPriorityRequest
from core.database import DatabaseDependency
from core.models import User, Priority
from core.service import is_current_user_admin

extra_router = APIRouter(prefix="/extra")

@extra_router.post("/add-priority",status_code=status.HTTP_201_CREATED)
async def add_priority(
    add_priority_request:AddPriorityRequest,
    current_user: User = Depends(is_current_user_admin),
    db: Session = Depends(DatabaseDependency())
    ):
    add_priority_model = Priority(
        name = add_priority_request.priority
        )
    db.add(add_priority_model)
    db.commit()


