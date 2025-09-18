from django.db import models

class Tag(models.Model):
    descricao = models.CharField(max_length=255, unique=True, null= True,
        blank= True)

    def __str__(self):
        return self.descricao


class CategoriaProduto(models.Model):
    descricao = models.CharField(
        max_length=255,
        unique=True,
        null= True,
        blank= True,
        default= 0
        )

    def __str__(self):
        return self.descricao


class Marca(models.Model):

    nome = models.CharField(
        max_length=25,
        null= True,
        blank= True,
        )
    
    descricao = models.TextField(
        null= True,
        blank= True,
        )

    def __str__(self):
        return self.nome


class Produto(models.Model):

    nome = models.CharField(
        max_length=255
        )
    
    tag = models.ForeignKey(
        Tag, 
        on_delete=models.CASCADE, 
        related_name="produtos", 
        null= True,
        blank= True,
        )
    
    categoria_produto = models.ForeignKey(
        CategoriaProduto,
        on_delete=models.CASCADE, 
        related_name="produtos", 
        null= True, 
        blank= True,)
    
    marca = models.ForeignKey(
        Marca, 
        on_delete=models.CASCADE, 
        related_name="produtos", 
        null= True,
        blank= True,
        )
    
    descricao = models.TextField(
        null= True,
        blank= True,
    )

    modelo = models.CharField(
        max_length=100, 
        null= True,
        blank= True,)
    
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2)
    
    imagem = models.ImageField(
        upload_to='produtos/', 
        null=True, blank=True)
    
    qt_estoque = models.IntegerField(
        null= True,
        blank= True,
    )


    def __str__(self):
        return self.nome

