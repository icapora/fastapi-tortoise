from app.models.base import Timestamp
from app.models.opinion import Opinion
from app.models.user import User
from tortoise import fields


class Like(Timestamp):
    id = fields.IntField(pk=True)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="likes"
    )
    opinion: fields.ForeignKeyRelation[Opinion] = fields.ForeignKeyField(
        "models.Opinion", related_name="likes"
    )
    like = fields.BooleanField(default=True)

    class Meta:
        table = "like"
        unique_together = ("user", "opinion")
