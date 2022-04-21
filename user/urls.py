from django.urls import path
from . views import ListItems, UserRegisterView,ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('register/',UserRegisterView.as_view(),name='register'),
    #user authenticated using jwt token
    # providing sufficient credentials such as email and password provides tokens such as access and refresh token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #providing  access token in bearer part and user id in url can update password of a user
    path('change_password/<int:pk>/',ChangePasswordView.as_view(),name='change-password'),

    path('list_items/',ListItems.as_view(),name='items')
]