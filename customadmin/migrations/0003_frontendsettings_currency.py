# Generated by Django 3.0.8 on 2021-02-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0002_auto_20210209_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontendsettings',
            name='currency',
            field=models.CharField(choices=[('tk', 'Tk'), ('dollar', '$')], default='tk', max_length=6),
        ),
    ]
