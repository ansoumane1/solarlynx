from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email', 'telephone', 'address', 'code_postal','city', 'country', 'note','transport'
        ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'telephone':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'code_postal':forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'note':forms.TextInput(attrs={'class':'form-control'}),
            'transport':forms.RadioSelect

        }