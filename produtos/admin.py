from django.contrib import admin
from .models import Produto, Venda

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin): # Cria uma classe no admin para o modelo Produto
    list_display = ('get_foto','id', 'nome', 'preco', 'estoque') # Campos a serem exibidos na lista de produtos
    search_fields = ('nome',) # Campos a serem pesquisados no admin

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin): 
    list_display = ('id', 'produto', 'quantidade')
    search_fields = ('produto__nome',)