# Generated by Django 3.2 on 2023-09-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventOrganizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Title')),
                ('short_description', models.TextField(blank=True, max_length=512, verbose_name='Short description')),
                ('long_description', models.TextField(blank=True, verbose_name='Long description')),
                ('longitude', models.FloatField(default=0, verbose_name='Longitude')),
                ('latitude', models.FloatField(default=0, verbose_name='Latitude')),
            ],
            options={
                'verbose_name': 'Организатор',
                'verbose_name_plural': 'Организаторы',
            },
        ),
    ]