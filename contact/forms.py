from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth import password_validation

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
    ), required = False)
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

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required= True
    )
    last_name = forms.CharField(
        required= True
    )
    email = forms.EmailField(
        required= True
    )
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'email', 
            'username', 
            'password1', 
            'password2',
            )
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email= email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Esse endereço de email já está sendo usado',
                    code= 'Invalid email'
                )
            )
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required= True)
    last_name = forms.CharField(required= True)
    email = forms.EmailField(required= True)
    username = forms.CharField(required= True)
    password1 = forms.CharField(
        required= False,
        label= 'Senha',
        strip= False,
        widget= forms.PasswordInput(attrs= {'autocomplete': 'new-password'}),
        help_text= password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        required= False,
        label= 'Confirme sua senha',
        strip= False,
        widget= forms.PasswordInput(attrs= {'autocomplete': 'new-password'}),
    )
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name',
            'email',
            'username',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True
            

    def save(self, commit= True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError(
                        'Senhas são diferentes'
                    )
                )
        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email= email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'Esse endereço de email já está sendo usado',
                        code= 'Invalid email'
                    )
                )
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(
                        errors,
                        code= 'Inválid',
                    )
                )
        return password1