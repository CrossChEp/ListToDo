from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controller.auth_controller import get_current_user
from entity.entities import UserEntity, GroupEntity
from factory import generate_session
from model.group.group_update_model import GroupUpdateModel
from service import group_service

group_controller = APIRouter()


@group_controller.post("/api/group")
def add_group(name: str, user: UserEntity = Depends(get_current_user),
              session: Session = Depends(generate_session)):
    return group_service.create_group(name, user, session)


@group_controller.post("/api/group/tasks")
def add_tasks_to_group(task_ids: list[int], group_id: int,
                       user: UserEntity = Depends(get_current_user),
                       session: Session = Depends(generate_session)):
    return group_service.add_tasks_to_group(task_ids, group_id, user, session)


@group_controller.put("/api/group")
def update_group(group_update_model: GroupUpdateModel, user: UserEntity = Depends(get_current_user),
                 session: Session = Depends(generate_session)):
    return group_service.update_group(group_update_model, user, session)


@group_controller.delete("/api/group/{group_id}")
def delete_group(group_id: int, user: UserEntity = Depends(get_current_user),
                 session: Session = Depends(generate_session)):
    return group_service.delete_group(group_id, user, session)
