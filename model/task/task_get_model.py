from entity.entities import TaskEntity
from model.task.task_update_model import TaskUpdateModel


class TaskGetModel(TaskUpdateModel):

    status: str

    @staticmethod
    def to_model(task: TaskEntity):
        return TaskGetModel(id=task.id, name=task.name, status=task.status, expiration_date=task.expiration_time)
