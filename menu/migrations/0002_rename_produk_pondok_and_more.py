# Generated by Django 4.2.6 on 2024-01-01 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='produk',
            new_name='Pondok',
        ),
        migrations.RenameField(
            model_name='pondok',
            old_name='namaproduk',
            new_name='namapondok',
        ),
    ]