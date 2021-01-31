from django import forms

class FormEmailPost(forms.Form):
    name = forms.CharField(max_length=30)
    sender = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)