from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
#Create a user
#Create a superuser
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('User must have an email address. ')
        if not username:
            raise ValueError('User must have a username.')
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password=None):
        user=self.create_user(
        email=self.normalize_email(email),
        username=username,
        password=password,
    )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user



def get_profile_image_filepath(self,filename):
    return f'profile_image/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "logo/logo.png"
# Create your models here.
class User(AbstractBaseUser):
    email                    =models.EmailField(unique=True,max_length=100)
    username                 =models.CharField(max_length=100,unique=True)
    date_joined              =models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login               =models.DateTimeField(verbose_name="last_login",auto_now=True)
    is_admin                 =models.BooleanField(default=False)
    is_active                =models.BooleanField(default=True)
    is_staff                 =models.BooleanField(default=False)
    is_superuser             =models.BooleanField(default=False)
    profile_image            =models.ImageField(max_length=255,upload_to=get_profile_image_filepath,null=True,blank=True,default=get_default_profile_image)
    hide_email               =models.BooleanField(default=False)

    object=MyAccountManager()
    USERNAME_FIELD  ='email'
    REQUIRED_FIELDS=['username']
    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def get_profile_image_name(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_image/{self.pk}/')]

class Message(models.Model):
    sender_id=models.ForeignKey(User,on_delete=models.CASCADE,null=False,default="unknown")
    message=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    #message_status=models.BooleanField()
    #receiver_id=models.ManyToManyField(User,related_name='reciver')
    #message_id=models.AutoField(primary_key=True)
    def __str__(self):
        return  f"{self.sender_id} {self.message} {self.created_at}"
