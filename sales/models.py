from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    Categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nomEmpresa = models.CharField(max_length=100)
    nombProducto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    url = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombProducto

