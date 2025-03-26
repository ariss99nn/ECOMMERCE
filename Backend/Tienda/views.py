from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

def es_admin(user):
    return user.is_superuser or user.groups.filter(name='Administrador').exists()

def es_empleado(user):
    return user.groups.filter(name='Empleado').exists()

def es_cliente(user):
    return user.groups.filter(name='Cliente').exists()

@login_required
@user_passes_test(es_admin, login_url='/acceso-denegado/')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
@user_passes_test(es_empleado, login_url='/acceso-denegado/')
def vista_empleado(request):
    return render(request, 'empleado_dashboard.html')

@login_required
@user_passes_test(es_cliente, login_url='/acceso-denegado/')
def vista_cliente(request):
    return render(request, 'cliente_dashboard.html')

def acceso_denegado(request):
    return render(request, 'acceso_denegado.html')
