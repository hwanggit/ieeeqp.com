# Generated by Django 2.2.5 on 2020-02-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20200112_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='report_num',
            field=models.CharField(choices=[('1', 'Week 5'), ('2', 'Week 7')], default='2', help_text='Choose a milestone report', max_length=50),
        ),
    ]
