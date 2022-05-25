import uuid

from django.db import models


class Fee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credit_fee = models.IntegerField(default=0.05)
    debit_fee = models.IntegerField(default=0.03)
    created_at = models.DateTimeField(auto_now_add=True)
