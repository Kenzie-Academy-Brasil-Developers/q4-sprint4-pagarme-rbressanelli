import uuid

from django.db import models


class Payable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=255)
    payment_date = models.DateTimeField()
    amount = models.FloatField()
    
    fee = models.ForeignKey(
        'fee.Fee', on_delete=models.CASCADE, related_name='payables'
    )
    
    seller = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='payables'
    )

    transaction = models.OneToOneField('transaction.Transaction', on_delete=models.CASCADE)
