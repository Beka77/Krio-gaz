from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_image/',
        verbose_name='Изображение профиля',
        blank=True, null=True,
        default=None
    )
    email = models.EmailField(null=False, max_length=255)
    def __str__(self):
        return f"{self.username}"
    