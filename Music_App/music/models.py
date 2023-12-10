from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


from Music_App.music.validators.validators import string_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2), string_validator],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(0),)
    )

    def __str__(self):
        return self.username


class Album(models.Model):
    GENRES = (
        ("POP_MUSIC", "Pop Music"),
        ("JAZZ_MUSIC", "Jazz Music"),
        ("RNB_MUSIC", "R&B Music"),
        ("ROCK_MUSIC", "Rock Music"),
        ("COUNTRY_MUSIC", "Country Music"),
        ("DANCE_MUSIC", "Dance Music"),
        ("HIP_HOP_MUSIC", "Hip Hop Music"),
        ("OTHER", "Other"),
    )

    album_name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=30,
        choices=GENRES
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(0.0)]
    )
