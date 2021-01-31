from django import forms
from .models import ModelComment

class FormComment(forms.ModelForm):
    class Meta:
        model = ModelComment
        fields = ('text', )

        widgets = {
            'text':forms.Textarea(attrs={
                'class':'comment__textarea',
                'placeholder':'Текст комментария',
                'data-autoresize':'true'})
        }
