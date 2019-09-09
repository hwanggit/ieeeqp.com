# Generated by Django 2.2.5 on 2019-09-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QPApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('personal_link', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('course_work', models.TextField(help_text='List any coursework relevant to building projects or working in teams!', max_length=3000)),
                ('extracurricular_work', models.TextField(help_text='List and describe up to 3 extracurricular projects or experiences', max_length=3000)),
                ('technical_skills', models.TextField(help_text='List any technical skills you have with a rating from 1 to 5 (eg: Photoshop (5),  AutoCAD (4), Python (3), Excel (1), etc.)', max_length=3000)),
                ('collab_situation', models.TextField(help_text='Describe a situation where you collaborated with others', max_length=3000)),
                ('project_motivation', models.TextField(help_text='In one to two sentences, what motivates you to be on a project? Why do you want to build a project, and what benefit does project experience bring to you and your teammates?', max_length=2000)),
                ('project_goal_but_not_steps', models.TextField(help_text='Imagine that you know the goal of your project but are unsure of the intermediate steps necessary to achieve it. What would you do to figure out these intermediate steps in order to progress and finish your project?', max_length=3000)),
                ('rude_team_member', models.TextField(help_text='You have a team member that is rude to your team members, does little work, and is in general hard to work with. How do you address this issue?', max_length=3000)),
                ('teammates', models.TextField(help_text='Hoping to work with other people? Please list their full name, email and major. (eg: John Smith, jsmith@gmail.com, ECE)', max_length=2000)),
                ('ieee_member_number', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
