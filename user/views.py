from django.shortcuts import render
from user.serializers import UserSerializer
from user.models import User
from rest_framework.generics import ListCreateAPIView


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
