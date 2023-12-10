from django import forms

from Music_App.music.models import Profile


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
