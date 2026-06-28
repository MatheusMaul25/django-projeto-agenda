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
            )
    def clean_first_name(self) -> dict[str, Any]:
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise ValidationError('Primeiro nome deve conter apenas letras!')
        return first_name
        
    def clean_last_name(self) -> dict[str, Any]:
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise ValidationError('Segundo nome deve conter apenas letras!')
        return last_name
            
    def clean_phone(self) -> dict[int, Any]:
         phone = self.cleaned_data.get('phone')
         if not phone.isdigit():
             raise ValidationError('Telefone inválido, digíte apenas números')
         if Contact.objects.filter(phone=phone).exists():
            raise ValidationError('Telefone já cadastrado')
         return phone
    
    def clean_email(self) -> dict[str, Any]:
        email = self.cleaned_data.get('email').lower()
        if Contact.objects.filter(email=email).exists():
            raise ValidationError('Email já cadastrado')
        return email
    