# Generated by Django 4.1.7 on 2023-03-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0025_product_tipo_alter_product_departamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='producto_imagen',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
