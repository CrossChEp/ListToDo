from sqlalchemy.orm import Session

from config.config import BASE_GROUP_NAME, NOT_DONE
from entity.entities import UserEntity, GroupEntity, TaskEntity
from exception.group_not_exists import GroupNotExists
from model.task.task_add_model import TaskAddModel


def add_task(task_data: TaskAddModel, user: UserEntity, session: Session):
    if not task_data.group_name:
        task_data.group_name = BASE_GROUP_NAME
    group: GroupEntity = find_user_group(task_data.group_name, user)
    task_data.group_name = group
    task = TaskEntity(name=task_data.name, status=NOT_DONE)
    group.tasks.append(task)
    session.add(task)
    session.commit()


def find_user_group(name: str, user: UserEntity):
    for group in user.task_groups:
        if group.name == name:
            return group
    raise GroupNotExists("user hasn't group with such name")
