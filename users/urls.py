from django.urls import path
from users.apps import UsersConfig
from users.views import UserUpdateAPI, PaymentListAPI

app_name = UsersConfig.name

urlpatterns = [
    path('user/update/<int:pk>/', UserUpdateAPI.as_view(), name='user_update'),

    path('payment/list/', PaymentListAPI.as_view(), name='payment_list'),
]
