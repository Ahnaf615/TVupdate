# Generated by Django 3.0.2 on 2020-01-27 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_auto_20200126_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodes',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='seasons',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='gallery'),
        ),
    ]
