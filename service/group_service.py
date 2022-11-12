from sqlalchemy.orm import Session

from entity.entities import UserEntity, GroupEntity, TaskEntity
from exception.group_already_exists import GroupAlreadyExists
from exception.group_not_exists import GroupNotExists
from model.group.group_update_model import GroupUpdateModel
from service import task_service, dto_service


def create_group(name: str, user: UserEntity, session: Session):
    group: GroupEntity = GroupEntity(name=name)
    if find_user_group(name, user):
        raise GroupAlreadyExists("user already has a group with such name")
    user.task_groups.append(group)
    session.add(group)
    session.commit()


def add_tasks_to_group(task_ids: list[int], group_id: int, user: UserEntity, session: Session):
    group: GroupEntity = get_group_by_id(group_id, session)
    if not group:
        raise GroupNotExists("group with such id doesn't exist")
    tasks = find_tasks(task_ids, user, session)
    for task in tasks:
        change_task_group(task, group)
    session.commit()
    return group


def find_tasks(task_ids: list[int], user: UserEntity, session: Session):
    tasks = []
    for task_id in task_ids:
        task = task_service.get_task_by_id(task_id, session)
        try:
            task_service.is_user_has_task_or_else_throw(task, user)
            tasks.append(task)
        except Exception:
            continue
    return tasks


def change_task_group(task: TaskEntity, group: GroupEntity):
    task.group = None
    group.tasks.append(task)


def update_group(new_group_data: GroupUpdateModel, user: UserEntity, session: Session):
    group: GroupEntity = get_group_by_id(new_group_data.id, session)
    if not group:
        raise GroupNotExists("group with such id is not found")
    if not find_user_group(group.name, user):
        raise GroupNotExists("user has no group with such id")
    group_req = session.query(GroupEntity).filter_by(id=new_group_data.id)
    new_group_data = convert_group_dto_to_dict(new_group_data)
    group_req.update(new_group_data)
    session.commit()
    return group


def convert_group_dto_to_dict(dto):
    dto_dict = dict()
    for key, value in dto.dict().items():
        if key == 'id' or dto.dict()[key] is None:
            continue
        dto_dict[key] = value
    return dto_dict


def find_user_group(name: str, user: UserEntity):
    for group in user.task_groups:
        if group.name == name:
            return group
    return None


def get_group_by_id(id: int, session: Session):
    return session.query(GroupEntity).filter_by(id=id).first()
