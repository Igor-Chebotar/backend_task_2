from django.db import models


class Mortgage(models.Model):
    bank_name = models.CharField(max_length=150, verbose_name='Наименование банка')
    payment = models.IntegerField(verbose_name='Первоначальный взнос')
    term_min = models.IntegerField(verbose_name='Срок ипотеки, ОТ')
    term_max = models.IntegerField(verbose_name='Срок ипотеки, ДО')
    rate_min = models.FloatField(verbose_name='Ставка, ОТ')
    rate_max = models.FloatField(verbose_name='Ставка, ДО')
    payment_min = models.IntegerField(verbose_name='Сумма кредита, ОТ')
    payment_max = models.IntegerField(verbose_name='Сумма кредита, ДО')

    class Meta:
        verbose_name = 'Ипотека'
        verbose_name_plural = 'Ипотеки'

