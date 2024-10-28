from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path
from users.apps import UsersConfig
from users.views import UserUpdateAPI, PaymentListAPI, UserListAPI, UserCreateAPI, UserRetrieveAPI, UserDestroyAPI

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user/create/', UserCreateAPI.as_view(), name='user_create'),
    path('user/list/', UserListAPI.as_view(), name='user_list'),
    path('user/detail/<int:pk>/', UserRetrieveAPI.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', UserUpdateAPI.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPI.as_view(), name='user_delete'),

    path('payment/list/', PaymentListAPI.as_view(), name='payment_list'),
]
