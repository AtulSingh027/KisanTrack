from django.urls import path
from .views import PostView, UpdatePost

urlpatterns = [
    path('api/posts/', PostView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', UpdatePost.as_view(), name='post-update-delete'),
]

