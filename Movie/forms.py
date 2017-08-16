from django import forms

from .models import Film, Actor, Genre

class PostForm(forms.ModelForm):

    class Meta:
        model = Film
        model = Actor
        model = Genre
        fields = ('Title', 'Decription','Year','Actor_name','Type')