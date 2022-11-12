from typing import Optional

from pydantic import BaseModel


class TaskAddModel(BaseModel):
    name: str
    group_name: Optional[str]

    class Config:
        orm_mode = True
