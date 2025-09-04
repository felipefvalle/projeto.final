from django.contrib import admin
from .models import Perfil, Endereco

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass
    

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    pass
