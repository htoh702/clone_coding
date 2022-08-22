from django.db import models
from django.contrib.auth.models import AbstractBaseUser     # 사용자 모델 패키지


class User(AbstractBaseUser):
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True, unique=True)
    user_id = models.CharField(max_length=30, blank=True, null=True)
    thumbnail = models.CharField(max_length=256, default='default_profile.jpg', blank=True, null=True)

    USERNAME_FIELD = 'id'               # 사용자의 이름값을 'id'필드로 사용한다
    REQUIRED_FIELDS = ['user_id']       # 사용자 데이터 필드

    def __str__(self):
        return self.user_id

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'users'

# Create your models here.
