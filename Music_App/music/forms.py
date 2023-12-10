from django import forms

from Music_App.music.models import Profile, Album


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

        widgets = {
            "album_name": forms.TextInput(attrs={"placeholder": "Album Name"}),
            "artist": forms.TextInput(attrs={"placeholder": "Artist"}),
            "description": forms.Textarea(attrs={"placeholder": "Description"}),
            "image_url": forms.TextInput(attrs={"placeholder": "Image URL"}),
            "price": forms.TextInput(attrs={"placeholder": "Price"}),

        }


class CreateAlbumForm(AlbumBaseForm):
    pass


class EditAlbumForm(AlbumBaseForm):
    pass
