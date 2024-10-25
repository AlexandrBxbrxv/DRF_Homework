from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


# Read Update для User ##############################################
class UserListAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPI(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Read для Payment ##################################################
class PaymentListAPI(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_filter = ('payment_date',)
