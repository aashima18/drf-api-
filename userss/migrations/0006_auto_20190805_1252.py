# Generated by Django 2.2.4 on 2019-08-05 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0005_auto_20190805_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='user_auth',
            new_name='user',
        ),
    ]
