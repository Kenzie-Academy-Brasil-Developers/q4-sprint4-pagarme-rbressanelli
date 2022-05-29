from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Fee
from .permissions import IsAdminUser
from .serializers import FeeSerializer


class FeeView(ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = Fee.objects.all()
    serializer_class = FeeSerializer


class FeeViewById(RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
