# Generated by Django 3.0.2 on 2020-01-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='department',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
