from django import forms
from django.contrib.auth.models import User
from .models import ModelProfile

class FormLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class FormUserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length='30', required=True)
    last_name = forms.CharField(max_length='30', required=True)

    class Meta:
        model = User
        fields = ('email', 'username')

        help_texts = {
            'username': None
        }
        
    def __init__(self, *args, **kwargs):
        super(FormUserRegistration, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.label = ''

        self.fields['email'].widget.attrs['placeholder'] = 'Ваш email'
        self.fields['username'].widget.attrs['placeholder'] = 'Ваше имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ваше имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ваша фамилия'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')

        return cd['password']

class FormProfile(forms.ModelForm):
    class Meta:
        model = ModelProfile
        fields = [
        'avatar',
        'date_of_birth',
        'background',
        'description',
        'about']

        widgets = {
            'about':forms.TextInput(attrs={
                'class':'account__input',
                'placeholder':'Напишите что-нибудь о себе',
                }),
            'description':forms.TextInput(attrs={
                'class':'account__input',
                'placeholder':'Напишите что-нибудь о своей деятельности',
                }),
        }

    def __init__(self, *args, **kwargs):
        super(FormProfile, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.label = ''

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'account__input',
                'placeholder':'Ваше имя',
                }),
            'last_name':forms.TextInput(attrs={
                'class':'account__input',
                'placeholder':'Ваша фамилия',
                }),
            'email':forms.TextInput(attrs={
                'class':'account__input',
                'placeholder':'Введите e-mail',
                }),
        }

    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.label = ''