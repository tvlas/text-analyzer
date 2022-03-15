from unicodedata import name
from django import forms


class UploadFile(forms.Form):
    form = forms.FileField(
        label='Arquivo txt', allow_empty_file=False, required=True,
    )
