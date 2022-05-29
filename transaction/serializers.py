from rest_framework import serializers

from .models import Transaction


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "amount",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "amount": {"read_only": True},
            "created_at": {"read_only": True},
        }
