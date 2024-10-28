from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

