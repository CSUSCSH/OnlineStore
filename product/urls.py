from django.conf.urls import url, include
from product import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'product_image', views.ProductImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]