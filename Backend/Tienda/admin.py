from django.contrib import admin
from .models import Proveedor, Categoria, Producto, Inventario, Venta, DetalleVenta, Carrito, CarritoItem

# Registro de modelos
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Carrito)
admin.site.register(CarritoItem)