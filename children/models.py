from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField, FileField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,
        related_name='profile')
    dp = ImageField(manual_crop="", blank=True)
    phone_number = models.BigIntegerField(null=True, unique=True)


    class Meta:
        ordering = ["-id"]
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username


class Guardians(models.Model):
    name = models.CharField(max_length=250)
    phoneNumber = models.BigIntegerField(null=True, unique=True)
    email = models.EmailField(max_length = 254)
    idNumber = models.BigIntegerField(null=True, unique=True)
    location = models.CharField(max_length=250)
    dp = ImageField(manual_crop="", blank=True)

    class Meta:
        ordering = ["-id"]

    def save_guardian(self):
        self.save()

    def delete_guardian(self):
        self.delete()

    def __str__(self):
        return self.name


class Children(models.Model):
    name = models.CharField(max_length=250)
    birth_cert_number = models.BigIntegerField(null=True, unique=True)
    birth_cert = FileField(blank=True)
    passport = ImageField(manual_crop="1024x1024", blank=True)
    guardian = models.ForeignKey(Guardians, on_delete=models.CASCADE,
        related_name='children', null=True, blank=True)


    class Meta:
        ordering = ["-id"]

    def save_child(self):
            self.save()

    def delete_child(self):
        self.delete()

    def __str__(self):
        return self.name