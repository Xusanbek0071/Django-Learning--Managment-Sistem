# Generated by Django 5.0 on 2023-12-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20200723_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]