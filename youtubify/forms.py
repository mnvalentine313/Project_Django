from django import forms
from .models import User, Video

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'profile')

class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('song', 'artist', 'video_url', 'user')