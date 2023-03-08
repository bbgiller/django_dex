# Generated by Django 4.1.7 on 2023-03-08 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dex_app', '0003_insulin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insulin',
            name='user_id',
        ),
        migrations.AddField(
            model_name='insulin',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dex_app.user'),
            preserve_default=False,
        ),
    ]
