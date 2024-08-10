from django.db import models

NULLABLE = {'blank': True, 'null': True}


class TableEntry(models.Model):
    date = models.DateField(verbose_name='дата')
    name = models.CharField(max_length=150, verbose_name='название')
    quantity = models.IntegerField(**NULLABLE, verbose_name='количество')
    distance = models.FloatField(**NULLABLE, verbose_name='расстояние')

    def __str__(self):
        return f'Таблица: {self.name}'

    class Meta:
        verbose_name = 'таблица'
        verbose_name_plural = 'таблицы'
