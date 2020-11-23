from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _ 
from PIL import Image

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("is_staff"), default=False)
    is_employee = models.BooleanField(_("is_employee"), default=False)
    is_employer = models.BooleanField(_("is_employer"), default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')



class Profile(models.Model):
    user =models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile')
    image =models.ImageField(upload_to='media/users', blank=True, null=True)
    birth_day = models.DateField(default=None, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    resume = models.TextField(blank=True)
    company =models.CharField(max_length=250, blank=True)


    def __str__(self):

        return self.user.first_name + " " + self.user.last_name
    

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image)

        if img.height >200 or img.width >200:
            new_size =(200,200)
            img.thumbnail(new_size)
            img.save(self.image.path)