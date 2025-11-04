from django.db import models
from products.models import Product
from django.urls import reverse


class AdCampaign(models.Model):
    CHANNEL_CHOICES = [
        ('social', 'Социальные сети'),
        ('search', 'Поисковая реклама'),
        ('email', 'Email-рассылка'),
        ('context', 'Контекстная реклама'),
        ('offline', 'Офлайн-реклама'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название кампании')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='campaigns',
        verbose_name='Рекламируемый продукт'
    )
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES, verbose_name='Канал продвижения')
    budget = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Бюджет на рекламу')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Рекламная кампания'
        verbose_name_plural = 'Рекламные кампании'
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.name} ({self.get_channel_display()})"

    def get_absolute_url(self):
        return reverse('ads:ad_campaign_detail', kwargs={'pk': self.pk})