# Generated by Django 2.2.5 on 2019-09-26 00:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0028_auto_20190926_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qpapplication',
            name='resume_upload',
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='num_of_scores',
            field=models.IntegerField(default=0, help_text='# of scorers', null=True),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='score',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
