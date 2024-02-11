from rest_framework import serializers
from .models import Categoria
from .models import Producto

class saleSerializerCategoria(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class saleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto

        fields = '__all__'
