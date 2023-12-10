from django.core.exceptions import ValidationError


def string_validator(value):
    for ch in value:
        if not ch.isalnum() and ch != "_":
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")