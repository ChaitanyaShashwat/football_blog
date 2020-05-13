from django import forms
from .models import Article


class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','slug','description','body','type','thumb']
        widgets = { 'title':forms.TextInput(attrs={'class': 'form-control'}),
                    'slug':forms.TextInput(attrs={'class': 'form-control'}),
                    'description':forms.Textarea(attrs={'class': 'form-control'}),
                    'body':forms.Textarea(attrs={'class': 'form-control'}),
                    'type':forms.Select(attrs={'class': 'form-control'})
                }
