from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controller.auth_controller import get_current_user
from entity.entities import UserEntity
from factory import generate_session
from model.user.user_add_model import UserAddModel
from model.user.user_get_model import UserGetModel
from service import user_service

user_controller = APIRouter()


@user_controller.post("/api/user/")
def register(user_data: UserAddModel, session: Session = Depends(generate_session)) -> UserGetModel:
    return user_service.add_user(user_data, session)
