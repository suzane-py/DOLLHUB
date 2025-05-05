from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario
from hashlib import sha256
from django.http import HttpResponse

# Create your views here.

def cadastro(request):
    status = request.GET.get('status') # Obtém o status da requisição GET
    return render(request, 'cadastro.html', {'status': status})

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0: # Verifica se o nome ou email estão vazios
        return redirect('/auth/cadastro/?status=1') # Redireciona para a página de cadastro com status 1 (campos obrigatórios)
    
    if len(senha) < 8: # Verifica se a senha tem menos de 8 caracteres
        return redirect('/auth/cadastro/?status=2') # Redireciona para a página de cadastro com status 2 (senha fraca)
    
    usuario = Usuario.objects.filter(email=email) # Verifica se o email já está cadastrado

    if len(usuario) > 0: # Se o email já estiver cadastrado, redireciona para a página de cadastro com status 3 (email já cadastrado)
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest() # Criptografa a senha usando SHA-256

        usuario = Usuario(nome=nome, 
                          email=email, 
                          senha=senha)
        
        usuario.save()
        return redirect('/auth/cadastro/?status=0') # Redireciona para a página de cadastro com status 0 (cadastro realizado com sucesso)
    except:
        return redirect('/auth/cadastro/?status=4') # Redireciona para a página de cadastro com status 4 (erro ao cadastrar)
    
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha) # Verifica se o email e a senha estão corretos

    if len(usuario) == 0: # Se o email ou a senha estiverem incorretos, redireciona para a página de login com status 1 (login inválido)
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0: 
        request.session['logado'] = True # Marca o usuário como logado
        return redirect('/produtos/home/') 
    else:
        return redirect('/auth/login/?status=2') # Redireciona para a página de login com status 2 (erro ao logar)
    
def logout(request):
    request.session['logado'] = None # Desmarca o usuário como logado
    return redirect('/auth/login/')



