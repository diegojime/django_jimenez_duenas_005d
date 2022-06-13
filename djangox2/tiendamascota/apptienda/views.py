from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm
# Create your views here.
def index(request):
    return render (request, 'index.html')
    
    
def ingresocliente(request):
    return render(request, "ingresocliente.html" )

def galeria(request):
    return render (request, 'galeria.html') 

def somos (request):
    return render(request, 'somos.html')

def api (request):
    return render(request, 'api.html')   

def formulario(request):
    return render(request, "formulario.html")

def ventaproductos(request):
    return render(request, 'ventaproductos.html')

def validacion(request):
    return render(request, "validacion.html")

def validacionContacto(request):
    return render(request, "validacionContacto.html")  

def formularioContacto(request):
    return render(request, "formularioContacto.html")


def ingresoweb(request):
    return render(request, "ingresoweb.html")

def login(request):
    return render(request, "login.html")


#-----------------------------------------------------------------------------------------------------------

def ventaproductos(request):
    producto = Producto.objects.all()
 

    datos = {
        'producto' : producto
    }
    return render(request, 'ventaproductos.html', datos)


def form_producto(request): 
    if request.method=='POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect ('ventaproductos')
    else:
        producto_form = ProductoForm()
    return render(request, 'agregarproductos.html', {'producto_form': producto_form})


def modificar(request, id):
    producto = Producto.objects.get(codigo=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect ('ventaproductos')
        
    return render(request, 'modificar.html', datos)


def form_eliminar(request,id):
    producto= Producto.objects.get(codigo=id)
    producto.delete()
    return redirect('ventaproductos')


def form_cliente(request): 
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('cliente')
    else:
        cliente_form = ClienteForm()
    return render(request, 'ingresocliente.html', {'cliente_form': cliente_form})


def cliente(request):
    cliente = Cliente.objects.all()
 

    datos = {
        'cliente' : cliente
    }
    return render(request, 'cliente.html', datos) 




def modificarcliente(request, id):
    cliente =  Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('cliente')
        
    return render(request, 'modificarcliente.html', datos)


def form_eliminar_cliente(request,id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('cliente')
