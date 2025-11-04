from django.db import models
from contracts.models import Contract
from django.urls import reverse


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name='customer',
        verbose_name='Контракт'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()

    def get_absolute_url(self):
        return reverse('customer_detail', kwargs={'pk': self.pk})

    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()