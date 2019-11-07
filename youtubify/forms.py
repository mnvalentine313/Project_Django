from django import forms
from django.forms import Textarea
from .models import User, Video

class UserForm(forms.ModelForm):
# Forms/Textarea widget resource: http://www.learningaboutelectronics.com/Articles/How-to-create-a-text-area-in-a-Django-form.php
    class Meta:
        model = User
        fields = ('username', 'profile')
        widgets = {
            'profile': Textarea(attrs={"rows": 3, "cols":50})
        }

class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('song', 'artist', 'video_url', 'user')