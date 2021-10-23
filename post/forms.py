from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    widget = forms.TextInput
    commenter = forms.CharField(widget=forms.TextInput())

    def get_attrs(self):
        return {
            'commenter': {'placeholder':'Your Name'},
            'commenter_email': {'placeholder':'Email Address'},
            'text': {'placeholder':'Please type what you want...'},
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        placeholders = self.get_attrs()
        for f_name, field in self.fields.items():
            html_attrs = {
                'class': 'form-control'
            }
            html_attrs.update(placeholders.get(f_name, {}))
            field.widget.attrs.update(html_attrs)

    class Meta:
        model = Comment
        fields = ['commenter', 'commenter_email', 'text']
