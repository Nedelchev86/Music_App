from django.contrib import admin

from Music_App.music.models import Profile


# Register your models here.


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass
