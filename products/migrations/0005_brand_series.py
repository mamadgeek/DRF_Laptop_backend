# Generated by Django 4.2.15 on 2024-09-05 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_brand_alter_laptopproduct_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='series',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
