# Generated by Django 5.0 on 2023-12-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0002_auto_20200907_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
