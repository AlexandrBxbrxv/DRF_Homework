from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path
from users.apps import UsersConfig
from users.views import UserUpdateAPI, PaymentListAPI, UserListAPI, UserCreateAPI, UserRetrieveAPI, UserDestroyAPI

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPI.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user/list/', UserListAPI.as_view(), name='user_list'),
    path('user/detail/<int:pk>/', UserRetrieveAPI.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', UserUpdateAPI.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPI.as_view(), name='user_delete'),

    path('payment/list/', PaymentListAPI.as_view(), name='payment_list'),
]
