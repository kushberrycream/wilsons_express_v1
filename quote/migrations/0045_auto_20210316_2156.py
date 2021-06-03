# Generated by Django 3.1.4 on 2021-03-16 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0044_auto_20210316_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='overall_volume',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Volume Weight'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='overall_weight',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Volume Weight'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='spec_service',
            field=models.CharField(max_length=20, verbose_name='Premium Services'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight',
            field=models.CharField(blank=True, default=0, max_length=10, verbose_name='Volume Weight'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight2',
            field=models.CharField(blank=True, default=0, max_length=10, verbose_name='Volume Weight'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight3',
            field=models.CharField(blank=True, default=0, max_length=10, verbose_name='Volume Weight'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight4',
            field=models.CharField(blank=True, default=0, max_length=10, verbose_name='Volume Weight'),
        ),
    ]
