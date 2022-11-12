from sqlalchemy.orm import Session

from entity.entities import UserEntity, GroupEntity
from exception.group_not_exists import GroupNotExists


def create_group(name: str, user: UserEntity, session: Session):
    group: GroupEntity = GroupEntity(name=name)
    user.task_groups.append(group)
    session.add(group)
    session.commit()


def find_user_group(name: str, user: UserEntity):
    for group in user.task_groups:
        if group.name == name:
            return group
    return False
