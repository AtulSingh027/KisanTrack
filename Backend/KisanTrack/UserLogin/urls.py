from django.urls import path
from .views import UserLogin, UserListCreate, UserDetail

urlpatterns = [
    path('login/', UserLogin.as_view(), name='user-login'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
