from rest_framework import serializers

from .models import Paymentinfo


class PaymentInfoSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):        
        ret = super().to_representation(instance)
        ret['card_number'] = ret['card_number'][-4:]
        return ret
    
    class Meta:
        model = Paymentinfo
        fields = '__all__'
        
        extra_kwargs = {
            'cvv': {'write_only': True},
            'is_active': {'default': True, 'required': False}         
        }        

