from django.shortcuts import render, redirect

from Music_App.music.forms import CreateUserForm
from Music_App.music.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]


def index(request):
    profile = get_profile()

    if not profile:
        return redirect("add profile")
    albums = Album.objects.all()

    context = {
        "albums": albums
    }
    return render(request, "core/home-with-profile.html", context)


def add_album(request):
    return render(request, "albums/add-album.html")


def edit_album(request, pk):
    return render(request, "albums/edit-album.html")


def delete_album(request, pk):
    return render(request, "albums/delete-album.html")


def details_album(request, pk):
    return render(request, "albums/album-details.html")


def details_profile(request):
    return render(request, "profiles/profile-details.html")


def delete_profile(request):
    return render(request, "profiles/profile-delete.html")


def add_profile(request):
    if request.method == "GET":
        form = CreateUserForm()
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form,
    }

    return render(request, "core/home-no-profile.html", context)
