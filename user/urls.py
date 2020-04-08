from django.conf.urls import url, include
from user import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'user_profile', views.UserProfileViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]