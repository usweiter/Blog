from django import forms
from .models import ModelStory

class FormAddStory(forms.ModelForm):
    class Meta:
        model = ModelStory
        fields = ('title', 'image')

        widgets = {
            'title':forms.TextInput(attrs={
                'placeholder':'Напишите что-нибудь',
                })
        }

    def __init__(self, *args, **kwargs):
        super(FormAddStory, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''