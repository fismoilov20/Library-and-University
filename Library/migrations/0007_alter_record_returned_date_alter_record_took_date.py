# Generated by Django 4.1 on 2022-09-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_alter_record_took_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='returned_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='took_date',
            field=models.DateField(),
        ),
    ]
