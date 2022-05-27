from rest_framework import serializers

from .models import Product
from user.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'seller', 'description', 'price', 'quantity', 'is_active', 
        ]
        
        extra_kwargs ={
            'is_active': {'read_only': True},
            'seller': {'read_only': True},
        }


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        extra_kwargs = {
            'description': {'required': False},
            'price': {'required': False},
            'quantity': {'required': False},
            "is_active": {"required": False},
            "seller": {"required": False},
        }


class ProductSellerSerializer(ProductSerializer):
    seller = UserSerializer(read_only=True)
