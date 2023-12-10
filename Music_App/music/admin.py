from django.contrib import admin

from Music_App.music.models import Profile, Album


# Register your models here.


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    pass
