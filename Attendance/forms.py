from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter student name', 'class': 'form-input'}),
            'roll_number': forms.TextInput(attrs={'placeholder': 'Enter roll number', 'class': 'form-input'}),
        }