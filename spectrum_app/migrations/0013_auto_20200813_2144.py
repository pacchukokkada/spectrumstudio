# Generated by Django 3.0.8 on 2020-08-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectrum_app', '0012_auto_20200812_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='days',
        ),
        migrations.AddField(
            model_name='booking',
            name='place',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
