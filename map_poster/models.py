from adminsortable.models import SortableMixin
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = HTMLField('Длинное описание')
    lat = models.FloatField(max_length=10, verbose_name='Широта')
    lon = models.FloatField(max_length=10, verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(SortableMixin):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )
    image = models.ImageField('Картинка')
    index = models.PositiveIntegerField(verbose_name='Номер картинки', blank=True, default=0)

    class Meta:
        ordering = ['index']

    def __str__(self):
        return self.place.title
