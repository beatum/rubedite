# Generated by Django 3.0.2 on 2020-06-19 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='id',
        ),
        migrations.AlterField(
            model_name='score',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
