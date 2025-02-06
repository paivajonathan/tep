from django.shortcuts import render, redirect
from .forms import MyForm
from .models import Person


def index(request):
    people = Person.objects.all().order_by('-id')
    return render(request, 'index.html', {'people': people})


def create(request):
    return render(request, 'create.html', {'form': MyForm()})


def store(request):
    # Caso store não seja chamado com verbo HTTP Post,
    # simplesmente mostra a rota de criação.
    if request.method != "POST":
        return redirect('create')
    
    form = MyForm(request.POST, request.FILES)
    
    # Caso o formulário tenha algum erro de validação,
    # renderiza a página de criação, com os erros de validação.
    if not form.is_valid():
        return render(request, 'create.html', {'form': form})
    
    data = request.POST
    files = request.FILES

    name = data.get('name')
    role = data.get('role')
    date_birth = data.get('date_birth')
    
    document = files.get('document')

    Person.objects.create(
        name=name,
        role=role,
        date_birth=date_birth,
        document=document,
    )

    # Caso tudo ocorreu bem, redireciona para a página de listagem
    return redirect('index')
