# Generated by Django 2.2.5 on 2019-09-25 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0025_auto_20190925_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpapplication',
            name='num_of_scores',
            field=models.IntegerField(default=0, help_text='# of scorers'),
            preserve_default=False,
        ),
    ]
