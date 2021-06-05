from django.db import models

# Create your models here.

class Fornecedor (models.Model):
   nome_fantasia = models.CharField(max_length=200)
   razao_social = models.CharField(max_length=200)
   cnpj = models.CharField(max_length=18)
   endereco = models.CharField(max_length=20)

   def __str__(self):
       return self.nome_fantasia 

class Cliente (models.Model):
   nome = models.CharField(max_length=200)
   cpf = models.CharField(max_length=14)
   data_nascimento = models.CharField(max_length=10)

   def __str__(self):
       return self.nome
