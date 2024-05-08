from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    age = models.IntegerField(
        default=0,
        verbose_name = 'Возраст',
    )
    balance = models.PositiveIntegerField(
        default=0,
        verbose_name = 'Баланс',
        blank=True, null=True
    )
    wallet_address = models.DateTimeField(
        max_length = 255,
        verbose_name = 'ID кошелька' 
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата регистрации' 
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


