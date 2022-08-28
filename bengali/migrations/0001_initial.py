# Generated by Django 3.2.13 on 2022-08-24 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bengali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=40)),
                ('lang', models.CharField(max_length=20)),
                ('quality', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hero', models.CharField(max_length=20)),
                ('heroine', models.CharField(max_length=20)),
                ('about', models.TextField()),
            ],
        ),
    ]