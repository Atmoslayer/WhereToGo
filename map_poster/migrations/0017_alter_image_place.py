# Generated by Django 3.2.18 on 2023-04-21 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map_poster', '0016_auto_20230413_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='map_poster.place', verbose_name='Место'),
        ),
    ]
