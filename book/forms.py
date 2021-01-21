from django import forms
from .models import Book

class BookForms(forms.ModelForm):


    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')

        author = forms.ModelMultipleChoiceField(queryset=Book.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'cols': '40', 'rows': '5', 'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
        }









