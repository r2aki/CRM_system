from django.db import models
from products.models import Product
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class Contract(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название контракта')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='contracts',
        verbose_name='Предоставляемый продукт'
    )
    document = models.FileField(
        upload_to='contracts/',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])],
        verbose_name='Файл документа'
    )
    start_date = models.DateField(verbose_name='Дата заключения')
    end_date = models.DateField(verbose_name='Период действия до')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.name} - {self.amount} руб."

    def get_absolute_url(self):
        return reverse('contract_detail', kwargs={'pk': self.pk})