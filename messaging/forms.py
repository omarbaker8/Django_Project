from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(),
        to_field_name='username',
        label="To"
    )
    content = forms.CharField(widget=forms.Textarea(attrs={'style': 'display: none;'}), required=False)

    class Meta:
        model = Message
        fields = ['recipient', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipient'].label_from_instance = lambda obj: obj.username

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content.strip():
            raise forms.ValidationError("Please enter a message before submitting.")
        return content