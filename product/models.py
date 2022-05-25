import uuid

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_Active = models.BooleanField()
    
    seller = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='products'
    )
