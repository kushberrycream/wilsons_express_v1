# Generated by Django 3.1.4 on 2021-03-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0033_quotelineitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='actual_weight',
        ),
        migrations.AlterField(
            model_name='quote',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='QuoteLineItem',
        ),
    ]
