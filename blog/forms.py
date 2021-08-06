from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        """Need to apply, which model we will use for creating forms.
           We can choose,which tables will be in our form."""
        model = Post
        fields = ('text', 'title',)