from distutils.archive_util import make_zipfile
from django.db import models

#class Oportunidade (models.Model): 
#    campus = models.CharField('Nome', max_length=100)
#    area = models.CharField('Nome', max_length=100)
#    tipo = models.CharField('Nome', max_length=100)
#    publico = models.CharField('Nome', max_length=100)

#class Usuario (models.Model): 
#    nome = models.CharField('Nome', max_length=100)
#    email = models.CharField('Email', max_length=100)
#    cpf = models.IntegerField('CPF')
#    matricula = models.IntegerField('Matricula')
#    datanascimento = models.IntegerField('Data de nascimento')
    
class Campus (models.Model):
    nome = models.CharField('Nome', max_length=100)
    
class Area (models.Model):
    nome = models.CharField('Nome', max_length=100)

class Tipo (models.Model):
    nome = models.CharField('Nome', max_length=100)