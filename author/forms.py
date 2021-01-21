from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')
        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'patronymic': 'Patronymic'
        }

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['patronymic'].required = False
