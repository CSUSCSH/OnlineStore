from rest_framework import serializers
from user.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(use_url=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'nickname', 'phone_number', 'avatar']
