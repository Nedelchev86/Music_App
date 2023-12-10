from django.forms import ModelForm

from Music_App.music.models import Profile


class CreateUserForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
