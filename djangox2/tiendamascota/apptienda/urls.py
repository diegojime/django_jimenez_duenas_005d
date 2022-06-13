from django.urls import path
from unicodedata import name 
from .views import form_cliente, form_eliminar, form_eliminar_cliente, form_producto, index, galeria, somos, api, formulario,  validacion, validacionContacto, ventaproductos, formularioContacto, modificar, ingresoweb, login, cliente, ingresocliente, modificarcliente

urlpatterns = [
     path('', index, name="index"),
     path('galeria/', galeria, name="galeria"),
     path('somos/', somos, name="somos" ),
     path('api/', api, name="api" ),
     path('formulario/', formulario, name="formulario"),
     path('formularioContacto/', formularioContacto, name="formularioContacto"),
     path('validacion/', validacion, name="validacion"),
     path('validacionContacto/', validacionContacto, name="validacionContacto"),
     path('ventaproductos/', ventaproductos, name="ventaproductos"),
     path('ingresoweb/', ingresoweb,  name="ingresoweb"),
     path('login/', login, name="login"),
     path('agregarproductos/', form_producto, name="agregarproductos"),
     path('modificar/<id>', modificar, name="modificar"),
     path('form_eliminar/<id>', form_eliminar, name="form_eliminar"),
     path('form_cliente/', form_cliente, name="form_cliente"),
     path('cliente/',cliente, name="cliente"),
     path('ingresocliente/',ingresocliente, name="ingresocliente"),
     path('modificarcliente/<id>',modificarcliente, name="modificarcliente"),
     path('form_eliminar_cliente/<id>', form_eliminar_cliente, name="form_eliminar_cliente")
]