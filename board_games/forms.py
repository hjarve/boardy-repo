from django import forms
from .models import BoardGame, Loan

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'description']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['borrow']
        labels = {'borrow': ''}