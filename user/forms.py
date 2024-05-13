from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text=" A vaild email adders please", required=True)

    class Meta:
        model = get_user_model()
        feilds = ["username", "password", "email"]

    def save(self, commit: bool = True):
        return super().save(commit)