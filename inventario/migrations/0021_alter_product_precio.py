# Generated by Django 4.1.7 on 2023-03-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0020_product_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
    ]