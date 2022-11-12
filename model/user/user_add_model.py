from pydantic import BaseModel


class UserAddModel(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True
