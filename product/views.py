from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from uuid import UUID

from user.serializers import UserSerializer

from .permissions import IsSellerUser
from .models import Product
from .serializers import ProductSellerSerializer, ProductSerializer, ProductUpdateSerializer
from user.models import User


def verify_uuid(uuid):    
    try:    
        uuid_obj =  UUID(uuid, version=4)
    except ValueError:
        return False
    return str(uuid_obj) == uuid


class ProductView(ListCreateAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSellerUser]
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def post(self, request: Request):
        
        user: User = request.user
        
        serializer = ProductSellerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.validated_data['seller'] = user
        product = Product.objects.create(**serializer.validated_data)
        
        serializer = ProductSellerSerializer(product)
        
        serializer.data['seller'] = UserSerializer(User.objects.filter(email=user.email).first()).data
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductViewById(RetrieveAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSellerUser]
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def patch(self, request: Request, pk):
        user: User = request.user
        
        if not verify_uuid(pk):
            return Response({'details': 'UUID must be a valid uuid'}, status=status.HTTP_400_BAD_REQUEST)
        
        price = request.data.get('price')
        quantity = request.data.get('quantity')
        
        if price and quantity:            
            if price < 0 or quantity < 0:
                return Response({'message': 'value must be 0 or greater'}, status=status.HTTP_400_BAD_REQUEST)        
        
        product = Product.objects.filter(id=pk)
        
        if not product:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if user.id == product[0].seller.id:
            serializer = ProductUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            product.update(**serializer.validated_data)
            serializer = ProductUpdateSerializer(product[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:            
            return Response({ "detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)


class GetProductBySellerId(ListAPIView):
    
      def get(self, request: Request, seller_id):
          
        if not verify_uuid(seller_id):
            return Response({'details': 'UUID must be a valid uuid'}, status=status.HTTP_400_BAD_REQUEST)  
          
        seller: User = User.objects.filter(id=seller_id).first()
        if not seller:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serialiser = ProductSerializer(
        Product.objects.filter(seller_id=seller_id), many=True
        )
        
        return Response(serialiser.data, status=status.HTTP_200_OK)
        