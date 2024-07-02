from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager
import os 
from apps.cart.models import Cart


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email addres')
        
        email= self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        shopping_cart = Cart.objects.create(user= user)
        shopping_cart.save()

        return user
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser= True
        user.is_staff = True
        user.save()

        return user
    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email= models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dni = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','dni', 'telefono','direccion']

    def get_full_name(self):
        return self.first_name + ' ' + self. last_name
    
    def get_short_name(self):
        return self.first_name
    
    def get_dni(self):
        return self.dni
    
    def get_telefono(self):
        return self.telefono
    
    def get_direccion(self):
        return self.direccion
    
    def __str__(self):
        return self.email