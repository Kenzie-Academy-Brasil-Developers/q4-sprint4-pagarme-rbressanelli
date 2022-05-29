import datetime

from rest_framework import serializers
from rest_framework.response import Response

from .models import Paymentinfo


class PaymentInfoSerializer(serializers.ModelSerializer):

    is_Active = serializers.SerializerMethodField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["card_number"] = ret["card_number"][-4:]
        return ret

    def get_is_Active(self, obj):
        if obj.card_expiring_date < datetime.datetime.now().date():
            obj.is_Active = False

        return obj.is_Active

    class Meta:
        model = Paymentinfo
        fields = "__all__"

        extra_kwargs = {
            "cvv": {"write_only": True},
            "is_Active": {"default": True, "required": False},
        }
