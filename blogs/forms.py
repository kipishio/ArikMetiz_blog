from django import  forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title':'Описание', 'text':'Пост'}

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'text-xl font-semibold text-gray-800 mb-2 w-full border border-gray-300 rounded px-3 py-2'
            }),
            'text': forms.Textarea(attrs={
                'class': 'text-gray-600 mb-4 w-full border border-gray-300 rounded px-3 py-2',
                'rows': 20,
            }),
        }