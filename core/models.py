from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, role, password=None, **extra_fields):
        if not email:
            raise ValueError('email must be provided')

        user = self.model(
            email=self.normalize_email(email),

            **extra_fields
        )
        user.set_password(password)
        user.role = 'admin'
        user.save()
        return user

    def create_superuser(self, email, password):

        if not email:
            raise ValueError('email must be provided')

        user = self.model(
            email=self.normalize_email(email)

        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model """

    """
        email: (username) ,
        name  , is_active  , is_staff
    """
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('reception', 'reception'),
        ('technician', 'technician'),
        ('inspector', 'inspector')
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name


class Part(models.Model):
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    is_repaired = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    part = models.ManyToManyField(Part)

    def __str__(self):
        return self.car_model
