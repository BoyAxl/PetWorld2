# Generated by Django 3.1.2 on 2020-11-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0008_auto_20201110_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='animal_id',
            field=models.ManyToManyField(to='producto.Animal'),
        ),
    ]