from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver

@receiver(post_migrate)
def crear_roles(sender, **kwargs):
    # Definimos los roles
    roles = ['Administrador', 'Empleado', 'Cliente']

    # Creamos los grupos si no existen
    for role in roles:
        group, created = Group.objects.get_or_create(name=role)

        # Asignar permisos (Ejemplo: para los empleados)
        if role == 'Empleado':
            permisos = Permission.objects.filter(content_type__app_label='Tienda')
            group.permissions.set(permisos)
        elif role == 'Cliente':
            # Los clientes no tendrán permisos administrativos
            group.permissions.clear()

    print("Roles creados o actualizados.")