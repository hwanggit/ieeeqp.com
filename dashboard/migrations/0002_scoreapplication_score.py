# Generated by Django 2.2.5 on 2019-09-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreapplication',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
