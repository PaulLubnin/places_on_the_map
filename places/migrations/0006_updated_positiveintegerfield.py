# Generated by Django 3.2 on 2023-11-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_required_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядковый номер'),
        ),
    ]
