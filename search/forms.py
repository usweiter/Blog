from django import forms

class FormSearch(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Поиск'}))