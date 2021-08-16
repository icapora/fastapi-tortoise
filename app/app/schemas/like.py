from typing import Optional

from pydantic import BaseModel


class LikeBase(BaseModel):
    opinion_id: Optional[int] = None
    user_id: Optional[int] = None


class LikeCreate(LikeBase):
    opinion_id: int
    user_id: int


class LikeUpdate(LikeBase):
    opinion_id: int
    user_id: int


class LikeInDBBase(LikeBase):
    id: int
    opinion_id: int
    user_id: int
    like: bool

    class Config:
        orm_mode = True


class Like(LikeInDBBase):
    pass


class OpinionInDB(LikeInDBBase):
    pass
