# Generated by Django 2.2.5 on 2019-10-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20191014_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectproposal',
            name='materials',
            field=models.CharField(help_text='Bill of Materials (Enter a new line for every item. Please provide: name, quantity, vendor-link for each)', max_length=2000),
        ),
        migrations.AlterField(
            model_name='projectproposal',
            name='timeline',
            field=models.CharField(help_text='Timeline of Work (Enter a new line for every week. Please provide: week # and task description for each)', max_length=2000),
        ),
    ]