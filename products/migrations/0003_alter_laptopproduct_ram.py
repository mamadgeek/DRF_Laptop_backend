# Generated by Django 4.2.15 on 2024-09-02 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_laptopproduct_gpu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptopproduct',
            name='ram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ram_laptops', to='products.ram'),
        ),
    ]
