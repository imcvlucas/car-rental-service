# Generated by Django 4.0.6 on 2022-09-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0009_alter_myuser_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mobile',
            field=models.IntegerField(blank=True),
        ),
    ]