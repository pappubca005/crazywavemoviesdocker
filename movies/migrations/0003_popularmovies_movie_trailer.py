# Generated by Django 4.2.3 on 2023-07-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_adlinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='popularmovies',
            name='movie_trailer',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]