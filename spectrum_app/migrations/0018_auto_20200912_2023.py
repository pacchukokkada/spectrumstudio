# Generated by Django 3.0.8 on 2020-09-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectrum_app', '0017_auto_20200905_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='weddingcouple',
            name='review',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='allphoto',
            name='main_photo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='sliderphoto',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='weddingcouple',
            name='main_photo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='weddingcouple',
            name='photographer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='weddingphoto',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='ShowCaseGallery',
        ),
        migrations.DeleteModel(
            name='ShowCasePhoto',
        ),
    ]