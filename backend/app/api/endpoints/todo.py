from fastapi import HTTPException, status, APIRouter, Depends, Query
from sqlalchemy.orm import Session
from core.schemas import AddTodoRequest, UpdateTodoRequest
from core.database import DatabaseDependency
from core.models import User, Todo
from core.service import get_current_user
from config.config import DEFAULT_PAGE_SIZE

todo_router = APIRouter(prefix="/todo")

@todo_router.get("/todos",status_code=status.HTTP_200_OK)
async def todo_list(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(DatabaseDependency()),
    page: int = Query(1, gt=0),
    page_size: int = Query(DEFAULT_PAGE_SIZE, gt=0)
    ):
    offset = (page -1 ) * page_size
    todos = db.query(Todo).filter(Todo.user_id == current_user.id).offset(offset).limit(page_size).all()
    return todos


@todo_router.post("/create",status_code=status.HTTP_201_CREATED)
async def create_todo(
    add_todo_request:AddTodoRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(DatabaseDependency())
    ):
    #  Get User Id
    user_id = db.query(User).filter(User.email == current_user.email).first()
    add_todo_model = Todo(
        todo_title = add_todo_request.todo_title,
        todo_description = add_todo_request.todo_description,
        priority_id = add_todo_request.priority_id,
        is_completed = False,
        user_id = user_id.id
        )
    db.add(add_todo_model)
    db.commit()


@todo_router.put("/update",status_code=status.HTTP_202_ACCEPTED)
async def update_todo(
    update_todo_request:UpdateTodoRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(DatabaseDependency())
    ):
    existing_todo = db.query(Todo).filter(Todo.id == update_todo_request.id).first()
    if not existing_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    existing_todo.todo_title = update_todo_request.todo_title
    existing_todo.todo_description = update_todo_request.todo_description
    existing_todo.priority_id = update_todo_request.priority_id
    existing_todo.is_completed = update_todo_request.is_completed
    existing_todo.user_id = current_user.id
    db.commit()


@todo_router.delete("/delete/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo_id : str,
    user: bool = Depends(get_current_user),
    db: Session = Depends(DatabaseDependency())
    ):
    existing_todo = db.query(Todo).filter(Todo.id == todo_id ).first()
    if not existing_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")
    db.delete(existing_todo)
    db.commit()

    

