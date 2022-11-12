from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controller.auth_controller import get_current_user
from entity.entities import UserEntity
from factory import generate_session
from model.task.task_add_model import TaskAddModel
from service import task_service

task_controller = APIRouter()


@task_controller.post("/api/task")
def add_task(task_data: TaskAddModel, user: UserEntity = Depends(get_current_user),
             session: Session = Depends(generate_session)):
    task_service.add_task(task_data, user, session)
