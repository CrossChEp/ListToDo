from sqlalchemy.orm import Session

from entity.entities import UserEntity, GroupEntity


def create_group(name: str, user: UserEntity, session: Session):
    group: GroupEntity = GroupEntity(name=name)
    user.task_groups.append(group)
    session.add(group)
    session.commit()
