from re import T
from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField, FileField
from django.core.validators import MinValueValidator, MaxValueValidator

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
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["id"]

    def save_guardian(self):
        self.save()

    def delete_guardian(self):
        self.delete()
        
    @classmethod
    def search_item(cls, search_term):
        results = cls.objects.filter(name__icontains=search_term)
        return results
    
    @classmethod
    def update_guardian(cls, id, name, phoneNumber, email, location, dp):
        cls.objects.filter(id=id).update(name=name, phoneNumber=phoneNumber, email=email,location=location, dp=dp)

    def __str__(self):
        return self.name


class Children(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=30, null=True)
    birth_cert_number = models.BigIntegerField(null=True, unique=True)
    birth_cert = FileField(blank=True)
    passport = ImageField(manual_crop="1024x1024", blank=True)
    guardian = models.ForeignKey(Guardians, on_delete=models.CASCADE,
        related_name='children', null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    school = models.CharField(max_length=100, blank=True)
    medical_records = models.FileField(blank=True)
    school_report = models.FileField(blank=True)
    
    class Meta:
        ordering = ["-id"]

    def save_child(self):
            self.save()

    def delete_child(self):
        self.delete()
        
    @classmethod
    def search_item(cls, search_term):
        results = cls.objects.filter(name__icontains=search_term)
        return results
    
    @classmethod
    def update_guardian(cls, id, name, passport, guardian):
        cls.objects.filter(id=id).update(name=name, passport=passport, guardian=guardian)

    def __str__(self):
        return self.name