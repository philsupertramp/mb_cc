# Generated by Django 2.0.8 on 2018-08-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20180812_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]