from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, User
from schemas import UserCreate, UserResponse
from fastapi import HTTPException

app = FastAPI()

Base.metadata.create_all(bind=engine)

# home
@app.get("/")
def home():
    return {"message": "API funcionando"}

# get all users
@app.get("/users", response_model=list[UserResponse])
def get_users():

    db = SessionLocal()
    
    try:
        users = db.query(User).all()
        return users
    finally:
        db.close()

# create user
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):

    db = SessionLocal()

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
def get_user(user_id: str):

    db = SessionLocal()

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
@app.put("/users/{user_id}")
def update_user(user_id: str, data: UserCreate):

    db = SessionLocal()

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

    return user

# delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: str):

    db = SessionLocal()

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