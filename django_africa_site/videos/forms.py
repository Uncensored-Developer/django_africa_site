from django import forms
from .models import Video, VideoCategory


class AddVideoForm(forms.ModelForm):

    class Meta:
        model = Video
        choices = [
            ('test', 'Test'),
            ('test', 'Test'),
            ('test', 'Test'),
            ('test', 'Test'),
        ]
        exclude = ['created', 'modify', 'thumbnail', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input--style-4'}),
            'description': forms.Textarea(attrs={
                'class': 'input--style-4',
                'style': 'width: 100%; height: 200px;'
            }),

            'tags': forms.TextInput(attrs={'class': 'input--style-4'}),
            'link': forms.HiddenInput()
        }
