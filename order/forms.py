from django import forms
from .models import Order

class OrderForms(forms.ModelForm):


    class Meta:
        model = Order
        fields = ('user', 'book',  'end_at', 'plated_end_at')
        widgets = {
            'end_at': forms.DateInput(format='%Y-%m-%dT%H:%M:%S', attrs={
                'type': 'datetime-local', 'class': 'form-control'}),
            'plated_end_at': forms.DateInput(format='%Y-%m-%dT%H:%M:%S', attrs={
                'type': 'datetime-local', 'class': 'form-control'}),

        }

        # event_date = DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])

        # author = forms.ModelMultipleChoiceField(queryset=Book.objects.all(),
        #                                 widget=forms.Select(attrs={'class': 'form-control'}))
        #
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'cols': '40', 'rows': '5', 'class': 'form-control'}),
        #     'count': forms.NumberInput(attrs={'class': 'form-control'}),
        # }

        # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        # book = models.ForeignKey(Book, on_delete=models.CASCADE)
        # created_at = models.DateTimeField(auto_now_add=True, editable=False)
        # end_at = models.DateTimeField(null=True)
        # plated_end_at = models.DateTimeField()