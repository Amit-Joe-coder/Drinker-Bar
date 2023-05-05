from django import forms
from mainapp.models import rate

class entry_form(forms.ModelForm):
    name=forms.CharField()
    taste=forms.CharField()
    color=forms.CharField()
    price=forms.IntegerField()
    class Meta:
        model=rate
        fields ="__all__"
