# Generated by Django 2.1.7 on 2019-02-16 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0002_auto_20190216_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodbankstock',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='bloodbankstock',
            name='longitude',
        ),
    ]
