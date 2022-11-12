from pydantic import BaseModel

from entity.entities import UserEntity


class UserGetModel(BaseModel):
    id: int
    name: str

    @staticmethod
    def to_model(user: UserEntity):
        return UserGetModel(id=user.id, name=user.name)

    class Config:
        orm_mode = True
