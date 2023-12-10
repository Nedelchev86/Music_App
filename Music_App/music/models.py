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
