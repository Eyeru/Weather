from django.forms import ModelForm, TextInput
from .models import Weather

class AreaForm(ModelForm):
    class Meta:
        model = Weather
        fields = ['area']
        widgets = {
            'area': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } 