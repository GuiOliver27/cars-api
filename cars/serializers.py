from rest_framework import serializers
from cars.models import Brand, Car


class BrandModelSerializer(serializers,BrandModelSerializer): # type: ignore
    class Meta:
        model = Brand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'