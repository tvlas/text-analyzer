from django import forms


class UploadFile(forms.Form):
    file = forms.FileField(
        label='Arquivo txt', allow_empty_file=False, required=True
    )