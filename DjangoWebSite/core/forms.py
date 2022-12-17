from django import forms
from .models import *


class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['title', 'file']


class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['title', 'message', 'file']


# class AddSendEmailForm(forms.Form):
#     email = forms.EmailField(max_length=200, label='Почта', widget=forms.TextInput(
#         attrs={
#             'placeholder': "Email",
#         }
#     ))
#     title = forms.CharField(max_length=255, label='Тема письма', widget=forms.TextInput(
#         attrs={
#             'placeholder': "Тема письма"
#         }
#     ))
#     message = forms.CharField(widget=forms.Textarea(
#         attrs={
#             'class': "input__file-blocks-text",
#             'name': "comment", 'id': "",
#             'cols': 40,
#             'rows': 3,
#             'placeholder': "Текст письма",
#         }),
#     )
#     files = forms.FileField(label='файлы (не обязательно)', required=False)
