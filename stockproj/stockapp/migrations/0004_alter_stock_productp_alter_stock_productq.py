# Generated by Django 4.1.7 on 2023-02-22 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0003_alter_stock_productname_alter_stock_productq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='productP',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='productQ',
            field=models.CharField(max_length=5),
        ),
    ]
