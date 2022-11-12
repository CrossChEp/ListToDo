from sqlalchemy.orm import Session, Query

from config.config import BASE_GROUP_NAME, NOT_DONE
from entity.entities import UserEntity, GroupEntity, TaskEntity
from exception.group_not_exists import GroupNotExists
from exception.task_not_exists import TaskNotExists
from model.task.task_add_model import TaskAddModel
from model.task.task_get_model import TaskGetModel
from model.task.task_update_model import TaskUpdateModel
from service import group_service


def add_task(task_data: TaskAddModel, user: UserEntity, session: Session):
    if not task_data.group_name:
        task_data.group_name = BASE_GROUP_NAME
    group: GroupEntity = group_service.find_user_group(task_data.group_name, user)
    if not group:
        raise GroupNotExists("user hasn't group with such name")
    task_data.group_name = group
    task = TaskEntity(name=task_data.name, status=NOT_DONE)
    if not task_data.expiration_date:
        task.expiration_time = task_data.expiration_date
    group.tasks.append(task)
    session.add(task)
    session.commit()


def update_task(new_task_model: TaskUpdateModel, user: UserEntity, session: Session):
    task: TaskEntity = get_task_by(new_task_model.task_id, session)
    task_id = task.id
    if not task:
        raise TaskNotExists("task with such id doesn't exists")
    if not find_user_task(task, user):
        raise TaskNotExists("user has not such task")
    task_query: Query = session.query(TaskEntity).filter_by(id=new_task_model.task_id)
    new_task_model = convert_task_model_to_dict(new_task_model)
    task_query.update(new_task_model)
    session.commit()
    task = get_task_by(task_id, session)
    return task


def get_task_by(id: int, session: Session):
    return session.query(TaskEntity).filter_by(id=id).first()


def find_user_task(task: TaskEntity, user: UserEntity):
    for group in user.task_groups:
        for group_task in group.tasks:
            if task.id == group_task.id:
                return group_task
    return None


def convert_task_model_to_dict(task_model):
    task_dict = {}
    for key, value in task_model.dict().items():
        if key == 'task_id' or value is None:
            continue
        task_dict[key] = value
    return task_dict
