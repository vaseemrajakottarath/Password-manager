from django.urls import path
from . views import ListItems, UserRegisterView,ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('register/',UserRegisterView.as_view(),name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/<int:pk>/',ChangePasswordView.as_view(),name='change-password'),

    path('list_items/',ListItems.as_view(),name='items')
]