# Generated by Django 2.1.7 on 2019-02-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_userdetail_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='latitude',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='hospital',
            name='longitude',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
