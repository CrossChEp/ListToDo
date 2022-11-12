from typing import Optional

from model.user.user_add_model import UserAddModel


class UserUpdateModel(UserAddModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True
