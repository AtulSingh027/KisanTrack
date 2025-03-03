from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post,User

class PostSerializer(ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "username": obj.user.username,  # Return username instead of just user ID
        }

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]