from distutils.archive_util import make_zipfile
from django.db import models

class Usuário 
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=100)
    cpf = models.IntegerField('CPF')
    matricula = models.IntegerField('Matricula')
    datanascimento = models.IntegerField('Data de nascimento')