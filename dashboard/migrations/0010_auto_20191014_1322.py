# Generated by Django 2.2.5 on 2019-10-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20191013_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectproposal',
            name='program',
            field=models.CharField(choices=[('qp', 'QP'), ('qp2', 'QP++')], default='qp', help_text='Program (QP or QP++)', max_length=50),
        ),
        migrations.AddField(
            model_name='projectproposal',
            name='team_num',
            field=models.CharField(default=None, help_text='Team Number', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectproposal',
            name='confidence',
            field=models.CharField(help_text='Collect a sentence from each member stating why you are confident you will succeed in making this project', max_length=2000),
        ),
        migrations.AlterField(
            model_name='projectproposal',
            name='team',
            field=models.CharField(help_text='Team Nickname', max_length=300),
        ),
    ]
