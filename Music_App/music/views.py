from django.shortcuts import render, redirect

from Music_App.music.forms import CreateUserForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
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
    if request.method == "GET":
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "albums/add-album.html", context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "GET":
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
        "album": album,
    }
    return render(request, "albums/edit-album.html", context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "GET":

        form = DeleteAlbumForm(instance=album)
        # for field in form.fields:
        #     form.fields[field].disabled = True
    else:

        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
        "album": album
    }

    return render(request, "albums/delete-album.html", context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        "album": album,
    }
    return render(request, "albums/album-details.html", context)


def details_profile(request):
    profile = Profile.objects.all()[0]
    albums = Album.objects.all()
    context = {
        "profile": profile,
        "albums": albums
    }
    return render(request, "profiles/profile-details.html", context)


def delete_profile(request):
    profile = Profile.objects.all()[0]
    print(profile.pk)
    if request.method == "GET":
        profile_to_delete = profile
    else:
        profile.delete()
        Album.objects.all().delete()
        return redirect('index')

    context = {
        "profile_to_delete": profile,

    }
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
        "no_profile": True
    }

    return render(request, "core/home-no-profile.html", context)
