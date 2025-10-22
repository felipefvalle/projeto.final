from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Produto, Protuto_Tag, Categoria


# ======================
# PÁGINA INICIAL
# ======================
def index(request):
    """
    Página inicial do sistema de estoque.
    """
    context = {'titulo': 'Bem-vindo à Gestão de Estoque!'}
    return render(request, 'estoque/index_estoque.html', context)


# ======================
# AUTENTICAÇÃO
# ======================

class CustomLoginView(LoginView):
    template_name = 'estoque/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('estoque:produto_list')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('estoque:login')


class RegisterView(CreateView):
    template_name = 'estoque/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('estoque:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


# ======================
# PRODUTOS
# ======================
@method_decorator(login_required, name='dispatch')
class ProdutoListView(ListView):
    model = Produto
    template_name = 'estoque/produto_list.html'
    context_object_name = 'produtos'
    ordering = ['nome']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class ProdutoTabelaListView(ListView):
    model = Produto
    template_name = 'estoque/produto_tabela_list.html'
    context_object_name = 'produtos'
    ordering = ['nome']
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'estoque/produto_detail.html'
    context_object_name = 'produto'


@method_decorator(login_required, name='dispatch')
class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    success_url = reverse_lazy('estoque:produto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Cadastrar Novo Produto'
        return context


@method_decorator(login_required, name='dispatch')
class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    success_url = reverse_lazy('estoque:produto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Editar Produto'
        return context


@method_decorator(login_required, name='dispatch')
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'estoque/produto_confirm_delete.html'
    success_url = reverse_lazy('estoque:produto_list')
    context_object_name = 'produto'


# ======================
# CATEGORIAS
# ======================
@method_decorator(login_required, name='dispatch')
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'estoque/categoria_list.html'
    context_object_name = 'categorias'
    ordering = ['identificacao']
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'estoque/categoria_detail.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = self.object.produtos.all()
        return context


@method_decorator(login_required, name='dispatch')
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'estoque/categoria_form.html'
    fields = ['identificacao', 'descricao']
    success_url = reverse_lazy('estoque:categoria-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Cadastrar Nova Categoria'
        return context


@method_decorator(login_required, name='dispatch')
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'estoque/categoria_update.html'
    fields = ['identificacao', 'descricao']
    success_url = reverse_lazy('estoque:categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Editar Categoria'
        return context


@method_decorator(login_required, name='dispatch')
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'estoque/categoria_delete.html'
    context_object_name = 'categoria'
    success_url = reverse_lazy('estoque:categoria-list')


# ======================
# TAGS
# ======================
@method_decorator(login_required, name='dispatch')
class TagListView(ListView):
    model = Protuto_Tag
    template_name = 'estoque/tag_list.html'
    context_object_name = 'tags'
    ordering = ['identificacao']
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class TagDetailView(DetailView):
    model = Protuto_Tag
    template_name = 'estoque/tag_detail.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos_relacionados'] = Produto.objects.filter(tag=self.object)
        return context


@method_decorator(login_required, name='dispatch')
class TagCreateView(CreateView):
    """
    View responsável por cadastrar uma nova Tag de produto.
    """
    model = Protuto_Tag
    template_name = 'estoque/tag_form.html'
    fields = ['identificacao', 'descricao']
    success_url = reverse_lazy('estoque:tags-list')  # redireciona para a lista após salvar

    def get_context_data(self, **kwargs):
        """
        Adiciona contexto extra para o template — usado no título e cabeçalho.
        """
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Cadastrar Nova Tag'
        context['button_text'] = 'Salvar Tag'
        context['cancel_url'] = reverse_lazy('estoque:tags-list')
        return context

    def form_valid(self, form):
        """
        Lógica adicional antes de salvar (caso queira adicionar logs ou mensagens).
        """
        response = super().form_valid(form)
        # Exemplo: enviar mensagem de sucesso se estiver usando Django messages
        # messages.success(self.request, "Tag criada com sucesso!")
        return response

@method_decorator(login_required, name='dispatch')
class TagUpdateView(UpdateView):
    model = Protuto_Tag
    template_name = 'estoque/tag_form.html'
    fields = ['identificacao', 'descricao']
    context_object_name = 'tag'
    success_url = reverse_lazy('estoque:tag-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Editar Tag'
        return context


@method_decorator(login_required, name='dispatch')
class TagDeleteView(DeleteView):
    model = Protuto_Tag
    template_name = 'estoque/tag_delete.html'
    context_object_name = 'tag'
    success_url = reverse_lazy('estoque:tag-list')



def RegistrarView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # autentica e loga o usuário automaticamente
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('categoria_list')  # já leva direto para categorias
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})

