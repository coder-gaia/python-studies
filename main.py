from fastapi import FastAPI
from database import engine, get_db
from models import Base, Task, User
from schemas import UserCreate, UserResponse, TaskCreate, TaskResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

app = FastAPI()

Base.metadata.create_all(bind=engine)

# home
@app.get("/")
def home():
    return {"message": "API funcionando"}

# get all users
@app.get(
    "/users",
    response_model=list[UserResponse]
)
def get_users(
    name: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(User)

    if name:
        query = query.filter(
            User.name.contains(name)
        )

    return query.all()

# create user
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# get user by id
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.id == user_id
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

# update user
@app.put(
    "/users/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: str,
    data: UserCreate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.name = data.name
    user.email = data.email

    db.commit()
    db.refresh(user)

    return user

# delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.id == user_id
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}

# create task
@app.post(
    "/users/{user_id}/tasks",
    response_model=TaskResponse
)
def create_task(
    user_id: str,
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_task = Task(
        title=task.title,
        user_id=user_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# get tasks by user
@app.get(
    "/users/{user_id}/tasks",
    response_model=list[TaskResponse]
)
def get_user_tasks(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user.tasks

# update task
@app.put(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id: str,
    data: TaskCreate,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.title = data.title

    db.commit()
    db.refresh(task)

    return task

# mark task as completed
@app.patch(
    "/tasks/{task_id}/complete",
    response_model=TaskResponse
)
def complete_task(task_id: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.completed = True

    db.commit()
    db.refresh(task)

    return task

# delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, db: Session = Depends(get_db)):
    
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted"
    }