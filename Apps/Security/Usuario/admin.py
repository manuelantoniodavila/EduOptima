from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from Apps.Security.Usuario.models import Usuario
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
 pass