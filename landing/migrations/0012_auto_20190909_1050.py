# Generated by Django 2.2.5 on 2019-09-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20190909_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qpapplication',
            name='ieee_member_number',
            field=models.CharField(blank=True, help_text='IEEE Member Number', max_length=100, null=True),
        ),
    ]
