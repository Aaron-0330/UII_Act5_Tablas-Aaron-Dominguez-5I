from django.db import models

# Create your models here.
class Usuario(models.Model):
    ROLES = (
        ('pasajero', 'Pasajero'),
        ('conductor', 'Conductor'),
    )

    nombre = models.CharField(max_length=100, help_text="Nombre completo del usuario")
    email = models.EmailField(unique=True, help_text="Correo electrónico del usuario (debe ser único)")
    telefono = models.CharField(max_length=15, blank=True, null=True, help_text="Número de teléfono del usuario")
    rol = models.CharField(max_length=10, choices=ROLES, default='pasajero', help_text="Rol del usuario en la plataforma")
    fecha_registro = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de registro del usuario")

    def __str__(self):
        return self.nombre