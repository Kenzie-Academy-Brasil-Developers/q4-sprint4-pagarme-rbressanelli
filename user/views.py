from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import Request, Response

from user.models import User
from user.permissions import IsAdminUser
from user.serializers import LoginSerializer, UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, _):
        serializer = UserSerializer(User.objects.all(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def login_view(request: Request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user: User = authenticate(**serializer.validated_data)

    if not user:
        return Response(
            {"detail": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST
        )

    token, _ = Token.objects.get_or_create(user=user)

    return Response({"token": token.key}, status=status.HTTP_200_OK)
