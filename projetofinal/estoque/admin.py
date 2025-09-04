from django.contrib import admin
from .models import Tag, CategoriaProduto, Marca, Produto

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoriaProduto)
class CategoriaProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    pass
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass
