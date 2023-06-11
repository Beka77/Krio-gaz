from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name="Name of site"
    )

    description = models.TextField(
        verbose_name= "description of site"
    )
    logo = models.ImageField(
        upload_to = "logo/"
    )
    facebook = models.URLField(
        verbose_name="facebook accaunt",
        blank = True, null = True
    )
    
    twitter = models.URLField(
        verbose_name="twitter accaunt",
        blank = True, null = True
    )
    pinterest = models.URLField(
        verbose_name="pinterest accaunt",
        blank = True, null = True
    )
    instagram = models.URLField(
        verbose_name="instagram accaunt",
        blank = True, null = True
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"


class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя")
    email = models.EmailField(
        verbose_name="Почта"
    )
   
    message = models.CharField(
        max_length=255, 
        verbose_name="Сообщение"
    )
    
    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"