# Generated by Django 2.2.4 on 2019-08-06 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0006_auto_20190805_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
