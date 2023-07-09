from django.db import models
from datetime import datetime
# Create your models here. taligado? todas as models -- representações das tabelas do bancos de dados
# Django tem um ORM proprio!!!!!!!

# a classe tem que herdar Model de models, pro django entender que isso é referente à uma tabela e conseguir processas as paradas.

# rodar python manage.py migrate, pro django criar as tabelas que ele mesmo precisa pra operar

class Categoria(models.Model):
    descricao = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    #Método mágico o.O
    def __str__(self):
        return self.descricao
    
    def total_gasto(self): #self é a referência da classe taligado?
        from extrato.models import Valores
        valores = Valores.objects.filter(categoria__id = self.id).filter(data__month=datetime.now().month).filter(tipo='S')
        total_valor = 0
        for valor in valores:
            total_valor += valor.valor
        return total_valor
    
    def calcula_percentual_gasto_por_categoria(self):
        try:
            return int((self.total_gasto() * 100) / self.valor_planejamento)
        except:
            return 0


class Conta(models.Model):
    banco_choices = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa Econômica'),
        ('BR', 'Bradesco'),
        ('ST', 'Santander')
    )

    tipo_choices = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica')
    )

    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to="icones")

    def __str__(self):
      return self.apelido
