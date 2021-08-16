from __future__ import annotations

from app.models.base import Timestamp
from app.models.user import User
from tortoise import fields


class Opinion(Timestamp):
    id = fields.IntField(pk=True)
    owner: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="opinions"
    )
    text = fields.CharField(max_length=255)
    reply_to: fields.ForeignKeyNullableRelation[Opinion] = fields.ForeignKeyField(
        "models.Opinion", related_name="comments", on_delete=fields.SET_NULL, null=True
    )

    comments: fields.ReverseRelation[Opinion]

    class Meta:
        table = "opinion"
