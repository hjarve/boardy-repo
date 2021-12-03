from django import forms
from django.db import models
from django.forms import fields

from .models import BoardGame

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'description']