# Generated by Django 2.2.5 on 2019-10-12 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_projectproposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectproposal',
            name='description',
            field=models.CharField(help_text='Project Description', max_length=2000),
        ),
        migrations.AlterField(
            model_name='projectproposal',
            name='materials',
            field=models.CharField(help_text='Bill of Materials (Eg: 1. Raspberry Pi B+, 3, www.amazon.com, 2. etc...)', max_length=2000),
        ),
        migrations.AlterField(
            model_name='projectproposal',
            name='timeline',
            field=models.CharField(help_text='Timeline of Work (Eg: Week 1 - Design, Week 2 - Build, Week 3 - Polish, etc...)', max_length=2000),
        ),
    ]
