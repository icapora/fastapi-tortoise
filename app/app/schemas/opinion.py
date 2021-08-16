from typing import Optional

from pydantic import BaseModel


class OpinionBase(BaseModel):
    text: Optional[str] = None


class OpinionCreate(OpinionBase):
    text: str


class OpinionUpdate(OpinionBase):
    text: str


class OpinionInDBBase(OpinionBase):
    id: int
    owner_id: int
    reply_to_id: Optional[int] = None
    text: str

    class Config:
        orm_mode = True


class Opinion(OpinionInDBBase):
    pass


class OpinionInDB(OpinionInDBBase):
    pass
