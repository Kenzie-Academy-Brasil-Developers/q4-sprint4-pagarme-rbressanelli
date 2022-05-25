from itertools import product
import uuid

from django.db import models


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    
    transaction = models.ForeignKey(
        'transaction.Transaction', on_delete=models.CASCADE, related_name='orders'
    )
    
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, related_name='orders'
    )
