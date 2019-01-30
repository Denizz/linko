from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LinkForm(forms.Form):
    title = forms.CharField(label='Название для линка', required=False)
    url = forms.URLField(label='Адрес линка', required=True)
    tags = forms.CharField(label='Теги (разделить пробелом)',required=False)

class SearchForm(forms.Form):
    keyword = forms.CharField(label='',required=True)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['keyword'].widget.attrs.update({'class': 'form-control search'})


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', required=True)
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Имя', required=False, help_text='Необязательное поле')
    last_name = forms.CharField(max_length=30, label='Фамилия', required=False, help_text='Необязательное поле')
    email = forms.EmailField(max_length=254, help_text='Обязательное для заполнения поле')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



