from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from payable.models import Payable

from .permissions import IsSellerUser
from .serializers import PayablesSerializer


class PayablesView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSellerUser]

    queryset = Payable.objects.all()
    serializer_class = PayablesSerializer

    def list(self, request, *args, **kwargs):

        seller_id = request.user.id

        payables = Payable.objects.filter(seller_id=seller_id).all()

        payment_amount_paid = 0
        payable_amount_waiting = 0

        for paid in payables:
            if paid.status == "paid":
                payment_amount_paid += paid.amount
            else:
                payable_amount_waiting += paid.amount

        output = {
            "payable_amount_paid": round(payment_amount_paid, 2),
            "payable_amount_waiting_funds": round(payable_amount_waiting, 2),
        }

        return Response(output, status=status.HTTP_200_OK)
