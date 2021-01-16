import datetime

from django import forms
from .models import Article,Comment


class AddblogForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'content','author')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text', 'person','article')
