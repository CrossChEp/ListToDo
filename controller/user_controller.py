from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controller.auth_controller import get_current_user
from entity.entities import UserEntity
from factory import generate_session
from model.user.user_add_model import UserAddModel
from model.user.user_get_model import UserGetModel
from model.user.user_update_model import UserUpdateModel
from service import user_service

user_controller = APIRouter()


@user_controller.post("/api/user/")
def register(user_data: UserAddModel, session: Session = Depends(generate_session)) -> UserGetModel:
    return user_service.add_user(user_data, session)


@user_controller.put("/api/user/")
def update_user(new_user_data: UserUpdateModel, session: Session = Depends(generate_session),
                user: UserEntity = Depends(get_current_user)):
    return user_service.update_user(new_user_data, user, session)
