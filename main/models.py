from datetime import datetime
from uuid import uuid4

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        if self.deleted_at is None:
            self.deleted_at = datetime.now()
            self.save()

    def hard_delete(self):
        super(BaseModel, self).delete()

    class Meta:
        abstract = True


class Definition(BaseModel):
    term = models.CharField(max_length=128)
    definition = models.TextField()

    class Meta:
        app_label = "main"
        db_table = "definition"

        indexes = [
            models.Index(fields=["term"]),
        ]
