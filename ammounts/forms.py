from django import forms
from .models import ProjectAccounts

class CreateForm(forms.ModelForm):
    class Meta:
        model = ProjectAccounts
        fields = ['Projectname', 'projectExpense']
