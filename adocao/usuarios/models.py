from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Animal(models.Model):
    TIPOS = [
        ('C', 'Cachorro'),
        ('G', 'Gato'),
        ('P', 'Pássaro'),
        ('R', 'Roedor'),
        ('O', 'Outros'),
    ]

    portes = [
        ('P', 'Pequeno')
        ('M', 'Médio')
        ('G', 'Grande')
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    idade = models.PositiveIntegerField()  # idade em anos
    porte = models.CharField(
        max_length=1, choices=portes, blank=True, null=True)
    cor = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_animais/', blank=True, null=True)
    data_resgate = models.BooleanField(default=False)
    abrigo = models.ForeignKey(
        'Abrigo', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome


class Adotante(models.Model):
    ESTADOS = [
        ('AC', 'Acre'),
        ('SP', 'São Paulo'),
        ('AL', 'Alagoas'),
        ('MG', 'Minas Gerais'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cidade = models.CharField(max_length=100)
    # adicione todos os estados conforme o necessario
    estado = models.CharField(max_length=2, choices=ESTADOS)

    def __str__(self) -> str:
        return self.nome


class Adocao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adotante = models.ForeignKey(Adotante, on_delete=models.CASCADE)
    data_adocao = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.animal.nome} - {self.adotante.nome}"


class Abrigo(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nome


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    abrigo = models.ForeignKey(
        Abrigo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
