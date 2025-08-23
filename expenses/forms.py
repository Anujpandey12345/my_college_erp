from django import forms
from .models import ComputerExpense, DailyExpense

class ComputerExpenseForm(forms.ModelForm):
    class Meta:
        model = ComputerExpense
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


from django import forms
from .models import DailyExpense

class DailyExpenseForm(forms.ModelForm):
    class Meta:
        model = DailyExpense
        exclude = ['user', 'date']  # date is auto and user is set in view
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
