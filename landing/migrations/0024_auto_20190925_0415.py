# Generated by Django 2.2.5 on 2019-09-25 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0023_remove_qpapplication_ieee_member_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qpapplication',
            options={'ordering': ['score']},
        ),
        migrations.AddField(
            model_name='qpapplication',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
