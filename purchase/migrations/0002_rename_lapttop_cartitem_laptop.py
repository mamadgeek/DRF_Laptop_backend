# Generated by Django 4.2.15 on 2024-09-06 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='lapttop',
            new_name='laptop',
        ),
    ]
