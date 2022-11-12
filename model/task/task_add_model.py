import datetime
from typing import Optional

from pydantic import BaseModel


class TaskAddModel(BaseModel):
    name: str
    expiration_date: Optional[datetime.date]
    group_name: Optional[str]

    class Config:
        orm_mode = True
