from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import saleSerializer
from .serializer import saleSerializerCategoria
from .models import Categoria
from .models import Producto
# Create your views here.

class view(viewsets.ModelViewSet):
    serializer_class_categoria = saleSerializerCategoria
    serializer_class = saleSerializer
    queryset = Categoria.objects.all()
    queryset = Producto.objects.all()