from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=50)
    description_short = models.CharField('Короткое описание', max_length=500)
    description_long = models.TextField('Длинное описание')

    def __str__(self):
        return self.title


class Coordinates(models.Model):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='place_coordinates'
    )
    lat = models.FloatField(max_length=10, verbose_name='Широта')
    lon = models.FloatField(max_length=10, verbose_name='Долгота')

    def __str__(self):
        return self.place.title


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='place_images'
    )
    image = models.ImageField('Картинка')
    index = models.IntegerField('Номер картинки')

    def __str__(self):
        return self.place.title