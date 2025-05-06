from django.db import models
from django.utils.safestring import mark_safe

class Produto(models.Model):
    foto = models.ImageField(upload_to='fotos', default='fotos/default.jpg') # Campo para armazenar a imagem do produto
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self): # Retorna o nome do produto quando chamado
        return self.nome
    
    @mark_safe # Marca a string como segura para ser renderizada como HTML
    def get_foto(self): # Retorna a tag HTML para exibir a imagem do produto
        return f"<img src='/media/{self.foto}' width='50' height='50'/>"

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE) # Relação de chave estrangeira com o modelo Produto, quando o produto for excluído, as vendas associadas também serão excluídas
    quantidade = models.IntegerField()
    
    def __str__(self):
        return f"{self.quantidade} de {self.produto.nome}" # Retorna a quantidade e o nome do produto vendido 