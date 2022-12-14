# Generated by Django 3.2.13 on 2022-08-26 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bengali', '0011_auto_20220826_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='BengWebseries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(default='WebSeries', max_length=20)),
                ('ribbon', models.CharField(default='<div class="ribbon-featured">New Release</div>', max_length=80)),
                ('name', models.CharField(default='', max_length=40)),
                ('lang', models.CharField(default='Bengali', max_length=20)),
                ('poster', models.ImageField(default='', upload_to='poster/bengali/webseries/')),
                ('quality', models.CharField(default='HD 1080', max_length=20)),
                ('spclnks', models.CharField(blank=True, default='#', max_length=40)),
                ('price', models.CharField(default='Free', max_length=20)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('hero', models.CharField(default='', max_length=20)),
                ('heroine', models.CharField(default='', max_length=20)),
                ('about', models.CharField(default='No About Updated', max_length=200)),
                ('watch', models.CharField(blank=True, default='bengwebseries', max_length=20)),
                ('embededlink', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
