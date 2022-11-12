from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controller.auth_controller import get_current_user
from entity.entities import UserEntity
from factory import generate_session
from model.task.change_color_model import ChangeColorModel
from model.task.task_add_model import TaskAddModel
from model.task.task_update_model import TaskUpdateModel
from service import task_service

task_controller = APIRouter()


@task_controller.post("/api/task")
def add_task(task_data: TaskAddModel, user: UserEntity = Depends(get_current_user),
             session: Session = Depends(generate_session)):
    task_service.add_task(task_data, user, session)


@task_controller.put("/api/task")
def update_task(new_task_data: TaskUpdateModel, user: UserEntity = Depends(get_current_user),
                session: Session = Depends(generate_session)):
    return task_service.update_task(new_task_data, user, session)


@task_controller.delete("/api/task/{task_id}")
def delete_task(task_id: int, user: UserEntity = Depends(get_current_user),
                session: Session = Depends(generate_session)):
    return task_service.delete_task(task_id, user, session)


@task_controller.post("/api/task/complete/{task_id}")
def complete_task(task_id: int, user: UserEntity = Depends(get_current_user),
                  session: Session = Depends(generate_session)):
    return task_service.complete_task(task_id, user, session)


@task_controller.post("/api/task/color")
def change_color(change_color_model: ChangeColorModel, user: UserEntity = Depends(get_current_user),
                 session: Session = Depends(generate_session)):
    return task_service.change_color(change_color_model, user, session)
