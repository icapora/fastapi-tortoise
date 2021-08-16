from tortoise import fields, models


class Timestamp(models.Model):
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True
