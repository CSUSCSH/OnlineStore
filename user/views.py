from django.contrib.auth import get_user_model
from rest_framework import viewsets
from user.models import UserProfile
from user.serializers import UserProfileSerializer

# User = get_user_model()


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
