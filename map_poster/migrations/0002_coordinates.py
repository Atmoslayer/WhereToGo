# Generated by Django 4.1.7 on 2023-03-24 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map_poster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_coordinates', to='map_poster.place', verbose_name='Место')),
            ],
        ),
    ]
