# Generated by Django 3.1.7 on 2022-03-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='trade_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Paymentnumber'),
        ),
    ]
