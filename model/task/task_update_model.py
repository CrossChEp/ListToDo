import datetime
from typing import Optional

from pydantic import BaseModel


class TaskUpdateModel(BaseModel):
    task_id: int
    name: Optional[str]
    expiration_date: Optional[datetime.date]

    class Config:
        orm_mode = True
