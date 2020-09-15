from django import forms
from tarin.models import trainer
import re


class trainFrom(forms.ModelForm):

    class Meta:
        model = trainer
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data('email')
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not (re.search(regex, email)):
            raise forms.ValidationError("not valid email")
        return email
