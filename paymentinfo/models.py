import uuid

from django.db import models


class Paymentinfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_method = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    cardholders_name = models.CharField(max_length=255)
    card_expiring_date = models.DateField()
    cvv = models.CharField(max_length=20)
    is_Active = models.BooleanField(default=True)

    customer = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="paymentinfo", null=True
    )
