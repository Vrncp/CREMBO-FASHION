# Generated by Django 4.1.7 on 2023-02-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_alter_products_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
