from django.contrib import admin
from .models import Animal, Adotante, Adocao, Abrigo

# Register your models here.


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'raca', 'idade', 'porte', 'adotado')
    list_filter = ('especie', 'porte', 'adotado')
    search_fields = ('nome', 'raca')


@admin.register(Adotante)
class AdotanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cidade', 'estado')
    list_filter = ('estado')
    search_fields = ('nome', 'email')


@admin.register(Adocao)
class AdocaoAdmin(admin.ModelAdmin):
    list_display = ('animal', 'adotante', 'data_adocao')
    search_fields = ('animal__nome', 'adotante__nome')
    list_filter = ('data_adocao')

@admin.register(Abrigo)
class AbrigoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado', 'telefone')
    search_fields = ('nome', 'cidade')
    list_filter = ('estado')
