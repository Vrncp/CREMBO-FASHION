# Generated by Django 4.1.7 on 2023-02-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_products_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='departamento',
            field=models.CharField(default=1, max_length=1),
        ),
    ]
