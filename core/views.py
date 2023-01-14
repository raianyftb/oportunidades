from django.shortcuts import render #, redirect
from .models import Campus, Area, Tipo, Usuario
from .models import CampusForm, AreaForm, TipoForm # Usuario


#def oportunidade(request):
#   oportunide = Oportunidades.objects.all()
#   contexto = {
#   'listar_oportunidades': oportunidades
#}


# def usuario(request):
#   usuario = Usuario.objects.all()
#    contexto = {
#        'listar_usuario': usuario
#    } 
#    return render(request, 'usuario.html', contexto)

def campus(request):
    campus = Campus.objects.all()
    contexto = {
        'listar_campus': campus
    } 
    return render(request, 'campus.html', contexto)

def Area 
    area = Area.objects.all()
    contexto = {
        'listar_area': area 
    } 
    return render(request, 'area.html', contexto)

def Tipo
    tipo = Tipo.objects.all()
    contexto = {
        'listar_tipo': campus
    } 
    return render(request, 'tipo.html', contexto)

def publico
    publico = Publico.objects.all()
    contexto = {
        'listar_publico': campus
    } 
    return render(request, 'publico.html', contexto) 



def area_cadastrar(request):
    form = AreaForm(resquest.POST or None)
    contexto = {
        'form':form
    }
    return render (request,'area_cadastrar' )


#def oportunidade(request):
#    form = OportunidadeForm(resquest.POST or None)
#    contexto = {
#        'form':form
#    }
#    return render (request,'oportunidade_cadastrar' )

#def cadastro(request):


#form = OportunidadeForm(request.POST or None)

#if form.is valid():
#    form.save()
#   return redirect('oportunidades')
    
#contexto = {
#    'form': form
#}
#return render (request, 'oportunidade_cadastrar.html', contexto)

