import bcrypt
from sqlalchemy.orm import Session, Query

from entity.entities import UserEntity
from exception.user_already_exists import UserAlreadyExists
from model.task.change_color_model import ChangeColorModel
from model.user.user_add_model import UserAddModel
from model.user.user_get_model import UserGetModel
from model.user.user_update_model import UserUpdateModel
from service import group_service


def add_user(user_data: UserAddModel, session: Session) -> UserGetModel:
    user: UserEntity = get_user_by_username(user_data.name, session)
    if user is not None:
        raise UserAlreadyExists("user with such name already exists")
    user_data.password = hash_password(user_data.password)
    user = UserEntity(**user_data.dict())
    group_service.create_group("base", user, session)
    session.add(user)
    session.commit()
    return UserGetModel.to_model(user)


def get_user_by_username(name: str, session: Session):
    return session.query(UserEntity).filter_by(name=name).first()


def get_user_by_id(id: int, session: Session):
    return session.query(UserEntity).filter_by(id=id).first()


def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def update_user(new_user_data: UserUpdateModel, user: UserEntity, session: Session) -> UserGetModel:
    new_user_data = convert_dto_to_dict(new_user_data)
    if get_user_by_username(new_user_data['name'], session):
        raise UserAlreadyExists("user with such name already exists")

    req: Query = session.query(UserEntity).filter_by(id=user.id)

    if new_user_data.get('password'):
        new_user_data['password'] = hash_password(new_user_data['password'])

    req.update(new_user_data)
    session.commit()
    return UserGetModel.to_model(user)


def convert_dto_to_dict(dto):
    dto_dict = dict()
    for key, value in dto.dict().items():
        if dto.dict()[key] is None:
            continue
        dto_dict[key] = value
    return dto_dict


def delete_user(user: UserEntity, session: Session) -> UserGetModel:
    session.delete(user)
    session.commit()
    return UserGetModel.to_model(user)
