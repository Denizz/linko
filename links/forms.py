from django import forms

class LinkForm(forms.Form):
    title = forms.CharField(label='Название для линка', required=False)
    url = forms.URLField(label='Адрес линка', required=True)
    tags = forms.CharField(label='Теги (разделить пробелом)',required=False)


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', required=True)
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput)



