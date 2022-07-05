from django import forms
from .models import RetailStore

class RetailModelForm(forms.ModelForm):
    class Meta:
        model = RetailStore
        fields = ('__all__')
        