import uuid

from django.db import models


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    payment_info = models.ForeignKey(
        "paymentinfo.Paymentinfo", on_delete=models.CASCADE, related_name="transactions"
    )

    seller = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="transactions"
    )
