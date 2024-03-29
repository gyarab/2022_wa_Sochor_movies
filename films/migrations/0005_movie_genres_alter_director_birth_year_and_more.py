# Generated by Django 4.1.7 on 2023-03-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='films.genre'),
        ),
        migrations.AlterField(
            model_name='director',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
