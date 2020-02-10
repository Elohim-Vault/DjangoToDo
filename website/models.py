from django.db import models

class Tarefa(models.Model):
    nome_tarefa = models.CharField(max_length=200)
    concluido = models.BooleanField()
    data_limite = models.DateField()

    def __str__(self):
        return self.nome_tarefa
