# Generated by Django 3.0.2 on 2020-03-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_auto_20200308_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodes',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
