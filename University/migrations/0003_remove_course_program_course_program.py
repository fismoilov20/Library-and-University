# Generated by Django 4.1 on 2022-09-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0002_alter_program_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='program',
        ),
        migrations.AddField(
            model_name='course',
            name='program',
            field=models.ManyToManyField(to='University.program'),
        ),
    ]
