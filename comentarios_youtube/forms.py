from django import forms
from .models import ComentarioYouTube

class ComentarioYouTubeForm(forms.ModelForm):
    class Meta:
        model = ComentarioYouTube
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }