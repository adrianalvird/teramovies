# Generated by Django 3.2.13 on 2022-08-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0004_auto_20220828_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engcinema',
            name='about',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='engcinema',
            name='embededlink',
            field=models.CharField(blank=True, default='#', max_length=500),
        ),
        migrations.AlterField(
            model_name='engcinema',
            name='hero',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='engcinema',
            name='heroine',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='english',
            name='about',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='english',
            name='embededlink',
            field=models.CharField(blank=True, default='#', max_length=500),
        ),
        migrations.AlterField(
            model_name='english',
            name='hero',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='english',
            name='heroine',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='engwebseries',
            name='about',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='engwebseries',
            name='embededlink',
            field=models.CharField(blank=True, default='#', max_length=500),
        ),
        migrations.AlterField(
            model_name='engwebseries',
            name='hero',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='engwebseries',
            name='heroine',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]