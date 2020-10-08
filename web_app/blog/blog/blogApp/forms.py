from django import forms

from blogApp.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {
            'title': 'Title',
            'text': 'Post'
        }
