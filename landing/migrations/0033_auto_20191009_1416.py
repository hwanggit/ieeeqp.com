# Generated by Django 2.2.5 on 2019-10-09 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0032_team_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qpapplication',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='landing.team'),
        ),
    ]
