from typing import Optional

from pydantic import BaseModel


class GroupUpdateModel(BaseModel):
    id: int
    name: Optional[str]
    color: Optional[str]
