from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm

from posts.models import Post

from django import forms

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email') 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group',)
