from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name='Codigo')
    marca= models.CharField(max_length=20, verbose_name='Marca')
    categoria= models.CharField(max_length=25, verbose_name='Categoria')

    def __str__(self):
        return self.codigo

class Cliente(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='nombre')
    apellido= models.CharField(max_length=25, verbose_name='apellido')
    correo= models.CharField(max_length=25, verbose_name='correo')
    rut= models.CharField(max_length=10, primary_key=True, verbose_name='rut')

    def __str__(self):
        return self.rut
# Create your models here.