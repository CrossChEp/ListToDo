from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

base = declarative_base()


class UserEntity(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    task_groups = relationship("GroupEntity", backref="task_group", cascade="all, delete-orphan")


class GroupEntity(base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    tasks = relationship("TaskEntity", backref="task")


class TaskEntity(base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    group = Column(Integer, ForeignKey('groups.id'))
