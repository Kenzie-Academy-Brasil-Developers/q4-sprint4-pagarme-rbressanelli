from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from datetime import timedelta
from rest_framework import status


from fee.models import Fee
from payable.models import Payable
from payable.serializers import PayablesSerializer
from product.models import Product
from .permissions import IsBuyerUser
from .models import Transaction
from .serializers import TransactionsSerializer
from order.models import Order
from paymentinfo.models import Paymentinfo
from user.models import User


class TransactionsView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsBuyerUser]

    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer

    def create(self, request, *args, **kwargs):

        informed_products = request.data["seller"]["products"]
        seller = request.data["seller"]["id"]
        paymentinfo = request.data["payment_info"]["id"]

        payment = Paymentinfo.objects.filter(id=paymentinfo).first()

        transactions = Transaction.objects.create(
            payment_info_id=paymentinfo, seller_id=seller
        )

        seller = User.objects.filter(id=seller).first()

        value = 0

        for product in informed_products:
            product_found = Product.objects.filter(id=product["id"]).first()

            Order.objects.create(
                quantity=product["quantity"],
                amount=product_found.price * product["quantity"],
                transaction=transactions,
                product=product_found,
            )
            product_found.quantity -= product["quantity"]
            product_found.save()
            value += product_found.price * product["quantity"]

        transactions.amount = value
        transactions.save()

        fee = Fee.objects.last()

        if payment.payment_method == "credit":
            payabledict = {
                "status": "waiting_funds",
                "payment_date": transactions.created_at + timedelta(days=30),
                "amount": transactions.amount - float(fee.credit_fee) * 100,
            }
        else:
            payabledict = {
                "status": "paid",
                "payment_date": transactions.created_at,
                "amount": transactions.amount - float(fee.debit_fee) * 100,
            }

        payable = Payable.objects.create(
            transaction=transactions, fee=fee, seller=seller, **payabledict
        )

        serializer = PayablesSerializer(payable)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        payables = Payable.objects.all()
        if request.user.is_seller:
            payables = payables.filter(seller_id=request.user.id).all()
        serializer = PayablesSerializer(payables, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
