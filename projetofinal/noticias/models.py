from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    descricao = models.CharField(max_length=255, unique=True, null= True,
        blank= True,)

    def __str__(self):
        return self.descricao


class CategoriaNoticia(models.Model):
    descricao = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.descricao


class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comentarios")
    noticia = models.ForeignKey('Noticia', on_delete=models.CASCADE, related_name="comentarios")
    conteudo = models.TextField( 
        null= True,
        blank= True,
    )
    status = models.CharField(max_length=10, choices=[('A', 'Aprovado'), ('P', 'Pendente'), ('R', 'Rejeitado')], default='P')

    def __str__(self):
        return f"Comentário de {self.user.username} na notícia {self.noticia.titulo}"


class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    conteudo = models.TextField()
    status = models.CharField(max_length=10, choices=[('A', 'Ativa'), ('I', 'Inativa')], default='A')
    tag = models.ManyToManyField(Tag, related_name="noticias")
    categoria_noticia = models.ForeignKey(CategoriaNoticia, on_delete=models.CASCADE, related_name="noticias")

    def __str__(self):
        return self.titulo
