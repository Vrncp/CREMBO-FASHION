# Generated by Django 4.1.7 on 2023-03-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='producto_imagen',
            field=models.ImageField(upload_to='images/'),
        ),
    ]