from django import forms

from .models import ClientDetail

class ClientDetailForm(forms.ModelForm):
    class Meta:
        model = ClientDetail
        fields = ['fname','lname','email','serialnumber','address','pcmodel','processor','ram','rom','amount']