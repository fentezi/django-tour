from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Город', unique=True)

    class Meta:
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Tour(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Из', to_field='name')
    in_city = models.CharField(max_length=50, verbose_name='В')
    hotel_title = models.CharField(max_length=50, verbose_name='Название отеля')
    star = models.IntegerField(verbose_name='Звезд у отеля', validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.URLField(verbose_name='Ссылка на фото')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='Описание')
    nights = models.IntegerField(verbose_name='Ночей', validators=[MinValueValidator(1)])
    date = models.DateField(verbose_name='Дата')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name_plural = 'Туры'
        ordering = ['city']

    def __str__(self):
        return self.hotel_title
