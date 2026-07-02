from django.shortcuts import render, get_object_or_404
from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from typing import Any
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder': 'Digíte seu primeiro nome'
    }),
    label= 'Primeiro Nome',
    max_length=50, 
    required=True,
    )

    phone = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder': 'Digite seu telefone',
    }),
    label = 'Telefone',
    required = True,
    help_text = 'Digíte apenas números',
    )

    picture = forms.ImageField(widget= forms.FileInput(
        attrs= {'accept': 'image/*',}
    ))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'placeholder': 'Primeiro nome'
    #     })

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
            )

    