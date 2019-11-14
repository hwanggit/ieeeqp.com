# Generated by Django 2.2.5 on 2019-10-24 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20191014_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_num', models.CharField(choices=[('1', 'Week 5'), ('2', 'Week 7')], default='1', help_text='Choose a milestone report', max_length=50)),
                ('team_num', models.IntegerField(help_text='Team Number (Please enter a number from 1 - 113)')),
                ('program', models.CharField(choices=[('qp', 'QP'), ('qp2', 'QP++')], default='qp', help_text='Program (QP or QP++)', max_length=50)),
                ('accomplishments', models.CharField(help_text='What have you accomplished so far?', max_length=2000)),
                ('projected', models.CharField(help_text='What do you hope to accomplish in the next 5 - 6 weeks?', max_length=2000)),
                ('blockers', models.CharField(blank=True, help_text='Name a few issues that are hindering/preventing your progress (Leave blank if none)', max_length=2000, null=True)),
            ],
        ),
    ]