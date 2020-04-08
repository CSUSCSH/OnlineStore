from rest_framework import serializers
from product.models import Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        return ProductImageSerializer(obj.image.all(), many=True, context={"request": self.context["request"]}).data

    class Meta:
        model = Product
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):

    # image_url = serializers.SerializerMethodField()
    image = serializers.ImageField(use_url=True)

    # def get_image_url(self, obj):
    #     return self.context['request'].build_absolute_uri(obj.image.url)

    class Meta:
        model = ProductImage
        fields = '__all__'
