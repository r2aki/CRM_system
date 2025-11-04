from django.db import models
from ads.models import AdCampaign
from django.urls import reverse


class Lead(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    campaign = models.ForeignKey(
        AdCampaign,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='leads',
        verbose_name='Рекламная кампания'
    )
    notes = models.TextField(blank=True, verbose_name='Примечания')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Потенциальный клиент'
        verbose_name_plural = 'Потенциальные клиенты'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()

    def get_absolute_url(self):
        return reverse('lead_detail', kwargs={'pk': self.pk})

    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()