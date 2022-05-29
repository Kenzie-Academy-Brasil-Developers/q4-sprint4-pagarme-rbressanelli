from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from .permissions import IsBuyerUser
from .models import Paymentinfo
from user.models import User
from .serializers import PaymentInfoSerializer


class PaymentMethodView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsBuyerUser]
    
    queryset = Paymentinfo.objects.all()
    serializer_class = PaymentInfoSerializer 
    
    def perform_create(self, serializer):
        serializer = serializer.save(customer=self.request.user)
              
        return serializer  
    
   
    def list(self, request: Request):
        user: User = request.user
        
        payments = Paymentinfo.objects.filter(customer_id=user.id).all()
        
        serializer = PaymentInfoSerializer(payments, many=True).data          
        
        return Response(serializer, status=status.HTTP_200_OK)        
