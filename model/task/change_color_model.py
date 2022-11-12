from pydantic import BaseModel


class ChangeColorModel(BaseModel):
    task_id: int
    color: str
