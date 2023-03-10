from django.urls import path
from .views import UserCreate,DetailUser, DeleteUser

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("<int:user_id>/", DetailUser.as_view(), name="DetailUser"),

    path('create/', UserCreate.as_view(),name='CreateUser'),
    
    path("delete/<int:user_id>/", DeleteUser.as_view(), name="DeleteUSer"),


]
