from pydantic import BaseModel


class Message(BaseModel):
    detail: str


class Status(BaseModel):
    status: str
