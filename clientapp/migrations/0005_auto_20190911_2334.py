# Generated by Django 2.2 on 2019-09-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0004_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
    ]
