from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class CustomUser(AbstractUser):
    name = CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.email or self.username

