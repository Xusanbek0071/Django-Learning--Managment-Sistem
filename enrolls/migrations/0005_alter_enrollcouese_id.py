# Generated by Django 5.0 on 2023-12-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolls', '0004_alter_enrollcouese_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollcouese',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
