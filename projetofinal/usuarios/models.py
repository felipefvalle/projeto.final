from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):

    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="perfil", 
        null= True,
        blank= True,
        )
    
    foto = models.ImageField(
        default='perfil_padrao.jpg', 
        upload_to='imagens_perfil',
        null=True, 
        blank=True
        )
    
    email = models.EmailField(
        unique=True
        )
    
    cpf = models.CharField(
        max_length=14, 
        unique=True
        )
    
    tel_fixo = models.CharField(
        max_length=15, 
        null=True, 
        blank=True
        )
    
    tel_celular = models.CharField(
        max_length=15, 
        null=True, 
        blank=True
        )
    
    data_de_nascimento = models.DateField(
        null= True, 
        blank= True,
        )
    
    genero = models.CharField(
        max_length=1, 
        choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')]
        )

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

class Endereco(models.Model):
    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="endereco", 
        null= True,
        blank= True,
        )
    
    cep = models.CharField(
        max_length=8
        )
    
    bairro = models.CharField(
        max_length=100
        )
    
    cidade = models.CharField(
        max_length=100
        )
    
    estado = models.CharField(
        max_length=2
        )
    
    logradouro = models.CharField(
        max_length=255
        )
    
    numero = models.CharField(
        max_length=20
        )
    
    complemento = models.CharField(
        max_length=255, 
        null=True, blank=True
        )

    def __str__(self):
        return f"Endereço de {self.usuario.username}"

