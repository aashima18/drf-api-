# Generated by Django 2.2.4 on 2019-08-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
