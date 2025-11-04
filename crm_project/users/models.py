from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    middle_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip() or self.username


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('operator', 'Оператор'),
        ('marketer', 'Маркетолог'),
        ('manager', 'Менеджер'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='manager', verbose_name='Роль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f"{self.user} - {self.get_role_display()}"