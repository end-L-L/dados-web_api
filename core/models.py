from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from django.core.validators import MinValueValidator

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"

class Profiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    alias = models.CharField(max_length=255,null=True, blank=True)
    born_date = models.DateField(auto_now_add=False, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return "Perfil de Usuario: "+ "Nombre: " +self.user.first_name+" Alias: "+self.alias
    
class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    n1w = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    n2w = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    n3w = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    n1l = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    n2l = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    n3l = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return "Record de Usuario: " + self.user.first_name

    def save(self, *args, **kwargs):
        self.wins = self.n1w + self.n2w + self.n3w
        self.losses = self.n1l + self.n2l + self.n3l
        super().save(*args, **kwargs)