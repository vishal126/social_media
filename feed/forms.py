from django import forms
from .models import *



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['caption']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write a comment...', 'rows': 1}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_profile

        fields = ['bio', 'profile_picture']
        