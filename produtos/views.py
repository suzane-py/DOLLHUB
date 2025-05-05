from django.shortcuts import render
from .models import Produto, Venda
from django.shortcuts import redirect

def home(request): # função para renderizar a página inicial
    if request.session['logado'] == True: # verifica se o usuário está logado
        produtos = Produto.objects.all() # obtém todos os produtos do banco de dados
        return render(request, 'home/home.html', {'produtos': produtos}) # recebe a requisição, renderiza o template 'home/home.html' e passa os produtos como contexto
    else:
        return redirect('/auth/login/?status=2')

def registrar_venda(request, produto_id):
    produto = Produto.objects.get(id=produto_id) # obtém o produto pelo ID fornecido na URL
    if request.method == 'POST':
        quantidade = request.POST.get('quantidade') 
        produto.estoque -= int(quantidade) 
        produto.save()

        venda = Venda(produto=produto, 
                      quantidade=quantidade) 
        venda.save()

        produtos = Produto.objects.all()
        return render(request, 'home/home.html', {'produtos': produtos})