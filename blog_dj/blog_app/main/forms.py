from .models import Post

from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
        widgets = {
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Name of Post"
        }),
        "text": Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Enter your text"
        }),
        
    }

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user