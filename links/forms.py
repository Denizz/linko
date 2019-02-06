from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('title', 'text', 'taglist')
        labels = {
            'title': 'Заголовок',
            'text': 'Адрес',
            'taglist': 'Ключевые слова (разделить пробелом)',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'taglist': forms.TextInput(attrs={'class': 'form-control'}),
        }



class SearchForm(forms.Form):
    keyword = forms.CharField(label='',required=True)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['keyword'].widget.attrs.update({'class': 'form-control search'})


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Имя', required=False, help_text='Необязательное поле')
    last_name = forms.CharField(max_length=30, label='Фамилия', required=False, help_text='Необязательное поле')
    email = forms.EmailField(max_length=254, help_text='Обязательное для заполнения поле')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



