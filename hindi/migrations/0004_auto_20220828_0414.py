# Generated by Django 3.2.13 on 2022-08-28 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindi', '0003_auto_20220826_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='hindi',
            name='ribbon',
            field=models.CharField(blank='True', default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='hincinema',
            name='ribbon',
            field=models.CharField(blank='True', default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='hinwebseries',
            name='ribbon',
            field=models.CharField(blank='True', default='', max_length=20),
        ),
    ]
