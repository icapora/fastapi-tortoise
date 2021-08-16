from app.models.base import Timestamp
from tortoise import fields


class User(Timestamp):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True, index=True)
    email = fields.CharField(max_length=62, unique=True, index=True)
    name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    hashed_password = fields.CharField(max_length=128, null=False)
    is_active = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)

    opinions: fields.ReverseRelation["Opinion"]  # type: ignore # noqa: F821
    likes: fields.ReverseRelation["Like"]  # type: ignore # noqa: F821

    class Meta:
        table = "user"
