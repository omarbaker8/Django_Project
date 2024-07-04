from django import forms
from .models import Comments,Project,User  

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': 'id_content'}), required=False)

    class Meta:
        model = Comments
        fields = ['content']
    # remove form-label class from labels
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ''



class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    stakeholders = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'}),
        required=False
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'status', 'stakeholders']