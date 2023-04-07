# Generated by Django 4.1.7 on 2023-04-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_poster', '0010_alter_image_options_remove_image_my_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['index']},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='image',
            name='object_id',
        ),
        migrations.AlterField(
            model_name='image',
            name='index',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Номер картинки'),
        ),
    ]
