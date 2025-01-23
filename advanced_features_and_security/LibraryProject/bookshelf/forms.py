from django import forms
from .models import Book  

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  
        fields = ['title', 'author', 'description']  
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
