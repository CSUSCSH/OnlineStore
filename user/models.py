from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, null=True, verbose_name='用户昵称')
    phone_number = models.CharField(max_length=16, null=True, verbose_name='手机号码')
    avatar = models.ImageField(upload_to='media/images/user/avatar/', max_length=200,
                               default='media/images/user/avatar/default_avatar.jpg', verbose_name='用户头像')

    def __str__(self):
        return self.username
