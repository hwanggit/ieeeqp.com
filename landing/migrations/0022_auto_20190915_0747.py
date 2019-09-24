# Generated by Django 2.2.5 on 2019-09-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0021_auto_20190912_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qpapplication',
            name='programs',
            field=models.CharField(choices=[('qp', 'Quarterly Projects'), ('qp2', 'QP++'), ('bo', 'Both')], default='qp', help_text='Which programs would you like to be considered for? *', max_length=50),
        ),
    ]