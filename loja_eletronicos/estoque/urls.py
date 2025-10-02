# imports
from django.urls import path 

# Importamos as views da nossa aplicação (o arquivo views.py)
from . import views 

# Define o "namespace" para a aplicação
app_name = 'estoque' 

urlpatterns = [
    # O caminho vazio '' significa a raiz da nossa aplicação 'produtos'
    path('', views.index, name='index'),
    path('teste/', views.teste, name='este'),

    ##
    # Produtos
    ##

    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/listar/', views.ProdutoTabelaListView.as_view(), name='produto_tabela_list'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categorias/novo/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categorias/<int:pk>/deletar/', views.CategoriaDeleteView.as_view(), name='categoria-delete'),
    path('tags/', views.TagListView.as_view(), name='tags-list'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag-detail'),
    path('tags/novo/', views.TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/editar/', views.TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/deletar/', views.TagDeleteView.as_view(), name='tag-delete'),

]
