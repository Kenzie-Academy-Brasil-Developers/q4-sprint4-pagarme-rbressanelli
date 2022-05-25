from rest_framework import serializers

from .models import Fee


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields =[
            'id', 'credit_fee', 'debit_fee', 'created_at',
        ]
