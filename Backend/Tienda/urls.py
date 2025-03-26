from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('empleado-dashboard/', views.vista_empleado, name='empleado_dashboard'),
    path('cliente-dashboard/', views.vista_cliente, name='cliente_dashboard'),
    path('acceso-denegado/', views.acceso_denegado, name='acceso_denegado'),
]