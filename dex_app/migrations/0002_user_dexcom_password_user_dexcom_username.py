# Generated by Django 4.1.7 on 2023-03-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dex_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dexcom_password',
            field=models.CharField(default=123456, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='dexcom_username',
            field=models.CharField(default=123456, max_length=100),
            preserve_default=False,
        ),
    ]
