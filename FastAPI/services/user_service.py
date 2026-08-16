from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserCreate


def create_user(db: Session, user_data: UserCreate):
   
    user = User(
        name=user_data.name,
        email=user_data.email,
        age=user_data.age
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_users(db: Session):
   
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
   
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def get_user_by_email(db: Session, email: str):
    
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def update_user(
    db: Session,
    user_id: int,
    user_data: UserCreate
):
    
    user = get_user_by_id(db, user_id)

    if not user:
        return None

    user.name = user_data.name
    user.email = user_data.email
    user.age = user_data.age

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):
    
    user = get_user_by_id(db, user_id)

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user