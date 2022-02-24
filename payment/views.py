import os

from alipay import AliPay
from django.http import HttpResponse,JsonResponse
# Initiate the payment interface and get the url of Alipay paymentl
# GET /orders/(?P<order_id>\d+)/payment/
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from backstage.models import cart
from sale import settings


class PayMentView(APIView):
    permission_classes = [IsAuthenticated]  # Only logged-in authenticated users can access

    def get(self, request, order_id):
        # Check if the order exists
        try:
            order = cart.objects.get(
                pk=order_id,  # order number
                user_id=request.user,  # Current user
            )
        except order.DoesNotExist:
            return JsonResponse({'message': 'Incorrect order information'})

        # Initiate a request to Alipay to obtain payment link parameters
        # Construct a payment object through the api (AliPay) in the sdk
        alipay_client = AliPay(
            appid=settings.ALIPAY_APPID,
            app_notify_url=None,  # default callback url
            # private key path specification
            app_private_key_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                              "app_private_key.pem"),
            # Alipay public key Path specification
            alipay_public_key_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                "alipay_public_key.pem"),  # Alipay's public key, used to verify Alipay's return message, not your own public key,
            sign_type="RSA2",  # RSA or RSA2
            debug=settings.ALIPAY_DEBUG  # Default False whether it is a sandbox environment
        )



        # For computer website payment, you need to jump to https://openapi.alipay.com/gateway.do? + order_string
        # The payment object calls the api (api_alipay_trade_page_pay) in the sdk to construct payment link parameters
        order_string = alipay_client.api_alipay_trade_page_pay(
            out_trade_no=order_id,  # order number
            total_amount=str(order.total_amount),  # total amount
            subject='test' % order_id,
            return_url="http://127.0.0.1:8000/done_s/",  # The page returned after successful payment
            notify_url=None  # Optional, if not filled, use the default notify url to inform the merchant's page whether the payment is successful or not
        )

        # Splicing payment link URL
        alipay_url = settings.ALIPAY_URL + '?' + order_string

        
        return JsonResponse({'alipay_url': alipay_url})
