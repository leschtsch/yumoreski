from .models import Jokes
from django.forms import ModelForm, Textarea


class JokesForm(ModelForm):
    class Meta:
        model = Jokes
        fields = ["text"]
        widgets = {
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст юморэски...',
            })
        }
