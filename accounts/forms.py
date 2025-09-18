from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="帳號", initial="sa")
    password = forms.CharField(label="密碼", widget=forms.PasswordInput(attrs={"value": "1qaz@WSX"}))