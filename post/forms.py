from django import forms
from .models import ModelPost
from trumbowyg.widgets import TrumbowygWidget

class FormAddPost(forms.ModelForm):
    class Meta:
        model = ModelPost
        fields = ('title', 'text', 'img', 'tags', 'status')

        widgets = {
            # 'img':forms.TextInput(attrs={
            #     'id':'id_img',
            #     'type':'file',
            #     'name':'img',
            #     'accept':'image/*'}),
            'title':forms.TextInput(attrs={
                'placeholder':'Заголовок',
                }),
            'text':TrumbowygWidget(attrs={
                'class':'add-post__textarea',
                'placeholder':'Напишите что-нибудь',
                }),
            'tags':forms.TextInput(attrs={
                'placeholder':'Список тегов через запятую.',
                }),
        }

    def __init__(self, *args, **kwargs):
        super(FormAddPost, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.label = ''

class FormFastAddPost(forms.ModelForm):
    class Meta:
        model = ModelPost
        fields = ('text', 'img')

        widgets = {
            'text':forms.Textarea(attrs={
                'class':'fast-add-post__textarea',
                'placeholder':'Напишите что-нибудь',
                'rows':1,
                'data-autoresize':'true'
                }),
        }

    def __init__(self, *args, **kwargs):
        super(FormFastAddPost, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.label = ''