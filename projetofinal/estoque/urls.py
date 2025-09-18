from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/listar', views.ProdutoTabelaListView.as_view(), name='produto_tabela_list'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),

]
