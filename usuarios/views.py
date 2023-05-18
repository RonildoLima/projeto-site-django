from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CadastroForm

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_realizado')
    else:
        form = CadastroForm()
    
    return render(request, 'usuarios/cadastro.html', {'form': form})

def cadastro_realizado(request):
    return render(request, 'usuarios/cadastro_realizado.html')

from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


