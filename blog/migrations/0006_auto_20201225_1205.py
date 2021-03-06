# Generated by Django 3.1.4 on 2020-12-25 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201224_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
