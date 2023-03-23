# Generated by Django 4.1 on 2023-03-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_stock_max_product_stock_min'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='form',
            field=models.CharField(choices=[('FLACON', 'FL'), ('BOITE', 'BT'), ('TUBE', 'TB'), ('CARTON', 'CT')], default='BOITE', max_length=20),
        ),
    ]