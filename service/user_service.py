import bcrypt
from sqlalchemy.orm import Session

from entity.entities import UserEntity
from exception.exceptions import UserAlreadyExists
from model.user.user_add_model import UserAddModel
from model.user.user_get_model import UserGetModel


def add_user(user_data: UserAddModel, session: Session) -> UserGetModel:
    user: UserEntity = get_user_by_username(user_data.name, session)
    if user is not None:
        raise UserAlreadyExists("user with such name already exists")
    user_data.password = hash_password(user_data.password)
    user = UserEntity(**user_data.dict())
    session.add(user)
    session.commit()
    return UserGetModel.to_model(user)


def get_user_by_username(name: str, session: Session):
    return session.query(UserEntity).filter_by(name=name).first()


def get_user_by_id(id: int, session: Session):
    return session.query(UserEntity).filter_by(id=id).first()


def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
