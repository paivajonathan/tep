# Generated by Django 5.1.5 on 2025-02-02 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='observation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
