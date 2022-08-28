# Generated by Django 3.2.13 on 2022-08-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='about',
            field=models.CharField(default='No About Updated', max_length=200),
        ),
        migrations.AlterField(
            model_name='home',
            name='embededlink',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='home',
            name='hero',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='heroine',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='lang',
            field=models.CharField(default='Bengali', max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='home',
            name='poster',
            field=models.ImageField(default='', upload_to='poster/home/'),
        ),
        migrations.AlterField(
            model_name='home',
            name='price',
            field=models.CharField(default='Free', max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='quality',
            field=models.CharField(default='2160 FHD', max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='spclnks',
            field=models.CharField(blank=True, default='#', max_length=40),
        ),
        migrations.AlterField(
            model_name='home',
            name='types',
            field=models.CharField(default='Cinema', max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='watch',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
