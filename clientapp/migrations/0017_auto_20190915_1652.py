# Generated by Django 2.2.5 on 2019-09-15 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0016_auto_20190915_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingtour',
            name='date_of_booking',
        ),
        migrations.RemoveField(
            model_name='bookingtour',
            name='number_of_people',
        ),
    ]
