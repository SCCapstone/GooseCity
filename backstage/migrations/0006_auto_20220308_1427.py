# Generated by Django 3.1.7 on 2022-03-08 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0005_user_info_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='flag',
            field=models.IntegerField(choices=[(0, 'Shopping cart'), (1, 'Buy')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='change_at',
            field=models.DateTimeField(auto_now=True, verbose_name='edir time'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='password',
            field=models.CharField(max_length=30, verbose_name='user pw'),
        ),
        migrations.CreateModel(
            name='credit_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('card_num', models.CharField(max_length=16)),
                ('date', models.DateField()),
                ('user_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_user', to='backstage.user_info')),
            ],
            options={
                'db_table': 'credit_card',
            },
        ),
    ]