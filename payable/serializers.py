from rest_framework import serializers

from payable.models import Payable


class PayablesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payable
        fields =[
            'id', 'amount'
        ]
