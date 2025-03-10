from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from users.users_schemas import User

class TestsGroupBase(BaseModel):
    nr_test: int
    tipo: Optional[str]

class TestsGroupCreate(TestsGroupBase):
    nr_test: int

class TestsGroupUpdate(TestsGroupBase):
    pass

class TestsGroup(TestsGroupBase):
    id: int

    class Config:
        from_attributes = True

class TestsGroupWithUser(TestsGroup):
    utente: User