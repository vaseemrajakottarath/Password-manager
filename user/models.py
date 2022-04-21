from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,name,phone_number,email,date_of_birth,password=None):
        if not email:
            raise ValueError('User must have an email address ')
        
        if not name:
            raise ValueError('User must have a name')

        user = self.model(
            email = self.normalize_email(email),
            name = name,
            phone_number=phone_number,
            date_of_birth=date_of_birth
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,name,phone_number,email,date_of_birth,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50,unique=True,blank=True)
    date_of_birth=models.DateField()
    


    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name','phone_number','date_of_birth']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_labels):
        return True

class Item(models.Model):
    item_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(Account,on_delete=models.CASCADE)