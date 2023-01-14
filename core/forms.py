from django.forms import ModelForm
from .models import Area, Campus, Tipo, Publico

class CampusForm (ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']

class AreaForm (ModelForm):
    class Meta:
        model = Area
        fields = ['nome']
        
class TipoForm (ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']
        
class PublicoForm (ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']
        
#class Oportunidade (MOdelForm):
#   class Meta:
#    model = Oportunidade
#    fields = ['Campus', 'Tipo', 'Area', 'Publico']


