from django.shortcuts import render
from .models import  Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()

    return render(request, "website/index.html", {"tarefas": tarefas})
