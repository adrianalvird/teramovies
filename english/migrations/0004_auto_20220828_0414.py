# Generated by Django 3.2.13 on 2022-08-28 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0003_auto_20220826_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='english',
            name='ribbon',
            field=models.CharField(blank='True', default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='engcinema',
            name='ribbon',
            field=models.CharField(blank='True', default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='engwebseries',
            name='ribbon',
            field=models.CharField(blank='True', default='', max_length=20),
        ),
    ]
