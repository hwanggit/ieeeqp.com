# Generated by Django 2.2.5 on 2019-10-12 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Project Title', max_length=100)),
                ('description', models.CharField(help_text='Project Description', max_length=1000)),
                ('team', models.CharField(help_text='Team Name', max_length=300)),
                ('materials', models.CharField(help_text='Bill of Materials (Eg: Raspberry Pi B+, 3, www.amazon.com)', max_length=300)),
                ('timeline', models.CharField(help_text='Timeline of Work (Eg: Week 1 - Design, Week 2 - Build, Week 3 - Polish)', max_length=300)),
            ],
        ),
    ]
