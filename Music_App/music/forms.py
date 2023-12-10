from django import forms

from Music_App.music.models import Profile, Album


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
