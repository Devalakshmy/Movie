from django import forms

from app1.models import Movie


class MovieForm(forms.ModelForm):
    class Meta: #inner class for defining form discription
        model=Movie #modelname
        fields='__all__' #all fields inside model