# Generated by Django 2.2.5 on 2019-09-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0017_auto_20190915_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtour',
            name='date_of_booking',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookingtour',
            name='number_of_people',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
