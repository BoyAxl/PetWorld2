# Generated by Django 3.1.2 on 2020-11-18 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0015_auto_20201117_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='animal_id',
            field=models.ManyToManyField(to='producto.Animal'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='', verbose_name='Imagen'),
        ),
    ]
